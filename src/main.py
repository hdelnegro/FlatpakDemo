import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FlatpakDemoApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="FlatpakDemo")
        self.set_default_size(300, 100)

        # Create a vertical box to hold the message and button
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Create a label with the welcome message
        label = Gtk.Label(label="Welcome to Flatpak!")
        vbox.pack_start(label, True, True, 0)

        # Create a close button
        close_button = Gtk.Button(label="Close")
        close_button.connect("clicked", self.on_close_button_clicked)
        vbox.pack_start(close_button, True, True, 0)

    def on_close_button_clicked(self, widget):
        Gtk.main_quit()

def main():
    app = FlatpakDemoApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()