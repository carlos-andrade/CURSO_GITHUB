#!/usr/bin/env python3
"""Valida estrutura básica e ligações relativas da documentação Markdown."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,}).*$", re.MULTILINE)


def remove_code_blocks(text: str) -> str:
    lines = text.splitlines()
    result = []
    fence = None
    for line in lines:
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker[0]
            elif marker[0] == fence:
                fence = None
            continue
        if fence is None:
            result.append(line)
    return "\n".join(result)


def main() -> int:
    markdown_files = sorted(ROOT.rglob("*.md"))
    errors = []
    if not markdown_files:
        print("ERRO: não foram encontrados ficheiros Markdown.")
        return 1

    for file_path in markdown_files:
        relative = file_path.relative_to(ROOT)
        content = file_path.read_text(encoding="utf-8").strip()
        if not content:
            errors.append(f"{relative}: ficheiro vazio")
            continue
        if not re.search(r"^#\s+\S", content, re.MULTILINE):
            errors.append(f"{relative}: falta um título H1")

        text = remove_code_blocks(content)
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            local_path = unquote(parsed.path)
            if local_path.startswith("/"):
                candidate = ROOT / local_path.lstrip("/")
            else:
                candidate = file_path.parent / local_path
            candidate = candidate.resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{relative}: ligação sai do repositório: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{relative}: destino local inexistente: {target}")

    if errors:
        print("Falhas de validação da documentação:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: {len(markdown_files)} ficheiros Markdown verificados; títulos e destinos das ligações locais válidos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
