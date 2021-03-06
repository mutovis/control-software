import os,sys

def main():
    if ('MUTOVIS_GUI_CONTROL' in os.environ) or ('-gui' in sys.argv[0]):
        from mutovis_control.gui.gui import gui
        g = gui()
        g.run()

    else:
        from mutovis_control.cli import cli
        c = cli()
        c.run()

if __name__ == "__main__":
    main()
