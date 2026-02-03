#!/usr/bin/env python3
import shlex
from pathlib import Path

INPUT_FILE = "swayidle_dotfile"
OUTPUT_FILE = "swayidle_dotfile_cmd.py"

def read_shell_commands(text: str) -> list[str]:
    """
    将 shell 文本解析为「每条完整命令一行」
    正确处理反斜杠续行
    """
    commands = []
    current = ""

    for line in text.splitlines():
        stripped = line.strip()

        # 跳过空行
        if not stripped:
            if current:
                commands.append(current.strip())
                current = ""
            continue

        if stripped.endswith("\\"):
            current += stripped[:-1] + " "
        else:
            current += stripped
            commands.append(current.strip())
            current = ""

    if current:
        commands.append(current.strip())

    return commands


def parse_to_argv(commands: list[str]) -> list[list[str]]:
    """
    将 shell 命令解析为 argv 形式
    """
    result = []
    for cmd in commands:
        argv = shlex.split(cmd, posix=True)
        result.append(argv)
    return result


def main():
    text = Path(INPUT_FILE).read_text(encoding="utf-8")

    shell_commands = read_shell_commands(text)
    argv_commands = parse_to_argv(shell_commands)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Auto-generated command list\n")
        f.write("COMMANDS = [\n")
        for cmd in argv_commands:
            f.write(f"    {cmd!r},\n")
        f.write("]\n")

    print(f"Parsed {len(argv_commands)} commands -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
