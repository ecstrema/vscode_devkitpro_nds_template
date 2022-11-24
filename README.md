# VSCode template for developping nintendo DS apps with devkitpro

## Steps to make this work:

### Install

Once you've started the codespace, run the `setup.sh` script in this readme's directory. Press enter to accept all prompts.

```bash
sudo ./setup.sh
```

If it doesn't work, try making the file executable with `chmod u+x`.

**Note that you may need to run the two last lines every time you open a new terminal instance.**

### Build

#### Using vscode

There is a task configured for this. Simply run the default build task. It will compile your project and open it in the emulator. (see the section "Forward your desktop" below).

Note that with the default keybindings, running the default build task can be done with `ctrl+shift+B`.

#### Using the command line

You can now build the executable using make:

```bash
source /etc/profile.d/devkit-env.sh # setup the shell
make
```

alternatively, to avoir re`source`ing `/etc/profile.d/devkit-env.sh` every time you open a new shell, use the `build.sh` script. Once again, you may have to make the file executable with `chmod u+x`.


### Forward your desktop

First, check that you have forwarded the desktop port: F1->Focus on ports view->noVNC should be running.

Open that adress in your browser using the little globe besides 127.0.0.1:... (hover to make it appear).

Login using "vscode" as password.

### Run

The emulator (desmume) can be run with `desmume` or `desmume-glade`

Now check your browser's vnc page: you should see it running there.

Click File->Open and find you compiled NDS file.

Click Emulation->Execute and enjoy!

## Q&A

### `setup.sh` an install-devkitpro-pacman file. Can I delete it?

Yes, you can safely delete it.

### How do you start a debugging session?

As much as I've tried, I did not manage to make debugging work properly. Help appreciated.
