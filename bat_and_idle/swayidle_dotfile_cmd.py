# Auto-generated command list
COMMANDS = [
    ['swayidle', 'timeout', '150', 'bat_state bat wlopm --off "*"', 'resume', 'wlopm --on "*"', 'timeout', '300', 'hyprlock', 'timeout', '600', 'bat_state bat bat_state more-than 25 systemctl suspend', 'timeout', '200', 'bat_state bat bat_state less-than 25 systemctl hybrid-sleep'],
    ['swayidle', '-w', 'before-sleep', 'hyprlock'],
]
