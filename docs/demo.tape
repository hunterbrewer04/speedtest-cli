# Records docs/demo.gif with https://github.com/charmbracelet/vhs
#
#   vhs docs/demo.tape            # run from the repo root; prefix VHS_NO_SANDBOX=true on Ubuntu 24.04+
#
# docs/demo-bin/speedtest stands in for Ookla's CLI and replays a made-up test, so the GIF needs no
# network and shows no real speeds, server, IPs or result link. Everything else is the real wrapper.

Output docs/demo.gif

Require python3

Set Shell "bash"
Set FontSize 16
Set Width 960
Set Height 480
Set Padding 24
Set Theme "Catppuccin Mocha"
Set TypingSpeed 45ms
Set WindowBar Colorful

# Off camera: clean prompt, the stand-in first on PATH, and `speedtest-cli` pointing at this checkout.
Hide
Type `export PS1='\[\e[1;35m\]$\[\e[0m\] ' PATH="$PWD/docs/demo-bin:$PATH"; alias speedtest-cli="$PWD/run_speedtest.py"; clear`
Enter
Show

Sleep 500ms
Type "speedtest-cli"
Sleep 600ms
Enter
Sleep 1s
Wait@60s /\$\s*$/
Sleep 6s
