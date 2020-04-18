#!/bin/env python3
# Este script cria o índice das dicas no README.

import os
import os.path
import re
from typing import Dict, List, Tuple


def obtem_topicos() -> Dict[str, List[Tuple]]:
    topicos: Dict[str, List[Tuple]] = {}

    for item_dir in sorted(os.listdir(".")):
        if not os.path.isdir(item_dir):
            continue
        if item_dir.startswith("."):
            continue

        if item_dir not in topicos:
            topicos[item_dir] = []

        for item_file in sorted(os.listdir(item_dir)):
            path = os.path.join(item_dir, item_file)
            if not os.path.isfile(path):
                continue
            if not item_file.endswith(".md"):
                continue

            with open(path) as fp:
                line = fp.readline().strip()

            m = re.match(r"# (.+)$", line)
            if m:
                title = m.group(1)
            else:
                raise ValueError("título inválido para {}".format(path))

            topicos[item_dir].append((item_file, title))

    return topicos


def atualiza_readme(topicos: Dict[str, List[Tuple]]) -> None:
    readme: List[str] = []
    readme.append("# tips\n")
    readme.append("\n")
    readme.append(
        "Este repositório contém algumas dicas de atalhos e tarefas específicas,\n"
    )
    readme.append("registradas para não se perderem no esquecimento.\n")
    readme.append("\n")

    for topico in topicos:
        readme.append("## {}\n".format(topico))
        readme.append("\n")
        for arquivo, titulo in topicos[topico]:
            readme.append(f"* [{titulo}]({topico}/{arquivo})\n")
        readme.append("\n")

    with open("README.md", "w") as fp:
        fp.writelines(readme)


if __name__ == "__main__":
    topicos = obtem_topicos()
    atualiza_readme(topicos)
