from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
# from playsound import playsound

mod = "mod4"
terminal = guess_terminal()
keys = [
    Key([mod], "u", lazy.spawn("flatpak run com.unity.UnityHub")),
    Key([mod], "x", lazy.spawn("gnome-boxes")),
    Key([mod], "e", lazy.spawn("obs")),
    Key([mod], "g", lazy.spawn("env LUTRIS_SKIP_INIT=1 lutris lutris:rungameid/1")),
    Key([mod], "b", lazy.spawn("/home/akil/upbge-0.36.1-linux-x86_64/blender")), 
    Key([mod], "s", lazy.spawn("steam")),
    Key([mod], "l", lazy.spawn("lutris")),
    Key([mod], "h", lazy.spawn("haguichi")),
    Key([mod], "v", lazy.spawn("steam steam://rungameid/438100")),
    Key([mod], "n", lazy.spawn("vivaldi")),
    Key([mod], "m", lazy.spawn("prismlauncher")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "Tab", lazy.spawn("pactl set-source-mute alsa_input.pci-0000_05_00.6.analog-stereo 1")),
    Key([mod], "F2", lazy.spawn("pactl set-source-mute alsa_input.pci-0000_05_00.6.analog-stereo 0")),
    Key([mod], "d", lazy.spawn("playerctl previous")),
    Key([mod], "a", lazy.spawn("playerctl next")),
    Key([mod], "r", lazy.spawn("playerctl play")),
    Key([mod], "q", lazy.spawn("playerctl pause")),
    Key([mod], "o", lazy.spawn("sudo reboot")),
    Key([mod], "p", lazy.spawn("sudo poweroff")),
    Key([mod], "F1", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +3%")),
    Key([mod], "F3", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -3%")),
    # Key([mod], "F3", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -3% && notify-send 'Volume' '$(pactl list sinks | grep "Volume:" | head -n 1 | awk '{print $5}')'")),
    # Key([mod], "F1", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +3% && notify-send 'Volume' '$(pactl list sinks | grep "Volume:" | head -n 1 | awk '{print $5}')'")),
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    # Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    # Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    # Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    # Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    # Key([mod, "shift"], "a", lazy.layout.shuffle_left(), desc="Move window to the left"),
    # Key([mod, "shift"], "d", lazy.layout.shuffle_right(), desc="Move window to the right"),
    # Key([mod, "shift"], "s", lazy.layout.shuffle_down(), desc="Move window down"),
    # Key([mod, "shift"], "w", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "shift"], "a", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "d", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "s", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "w", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key(
    #     [mod, "shift"], 
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    # Key(
    #     [mod],
    #     "f",
    #     lazy.window.toggle_fullscreen(),
    #     desc="Toggle fullscreen on the focused window",
    # ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "Shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "Shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=0),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
#     font="sans",
#     fontsize=12,
#     padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
     Screen(
#         bottom=bar.Bar(
#             [
#                  widget.CurrentLayout(),
#                  widget.GroupBox(),
#                  widget.Prompt(),
#                  widget.WindowName(),
#                  widget.Chord(
#                      chords_colors={
#                          "launch": ("#ff0000", "#ffffff"),
#                      },
#                      name_transform=lambda name: name.upper(),
#                  ),
#                  widget.TextBox("default config", name="default"),
#                  widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
#                  # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
#                  # widget.StatusNotifier(),
#                 widget.Systray(),
#                 widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
#                 widget.QuickExit(),
#             ],
#             24,
#             # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
#             # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
#         ),
#          You can uncomment this variable if you see that on X11 floating resize/moving is laggy
#          By default we handle these events delayed to already improve performance, however your system might still be struggling
#          This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
#          x11_drag_polling_rate = 60,
     ),
 ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
# floating_layout = layout.Floating(
#     float_rules=[
#         # Run the utility of `xprop` to see the wm class and name of an X client.
#         *layout.Floating.default_float_rules,
#         Match(wm_class="confirmreset"),  # gitk
#         Match(wm_class="makebranch"),  # gitk
#         Match(wm_class="maketag"),  # gitk
#         Match(wm_class="ssh-askpass"),  # ssh-askpass
#         Match(title="branchdialog"),  # gitk
#         Match(title="pinentry"),  # GPG key password entry
#     ]
# )
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
# Iniciar o programas
qtile.cmd_spawn("vivaldi")
qtile.cmd_spawn("rm -r /home/akil/.local/share/Trash/files")
qtile.cmd_spawn("rm -r /home/akil/.local/share/Steam/steamapps/compatdata/438100/pfx/drive_c/users/steamuser/AppData/LocalLow/VRChat/VRChat/Cache-WindowsPlayer")
qtile.cmd_spawn("rm -r /var/log")
qtile.cmd_spawn("rm -r ~/.cache")
qtile.cmd_spawn("rm -r /tmp")
qtile.cmd_spawn("lxpolkit")
qtile.cmd_spawn('easyeffects --gapplication-service')
qtile.cmd_spawn("feh --bg-fill https://r4.wallpaperflare.com/wallpaper/151/452/892/makoto-shinkai-kimi-no-na-wa-anime-landscape-wallpaper-f8f6ddc8f0a0ac88207c814eb882743a.jpg")
# qtile.cmd_spawn("playsound('/home/akil/Downloads/python/musicaPlaysound/yourmane.mp3')")
qtile.cmd_spawn("/home/akil/Downloads/Akil.sh")