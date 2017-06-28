import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        Gtk.Window.resize(self ,1000, 600)

        grid = Gtk.Grid(margin=30)
        self.add(grid)


        grid.set_column_spacing(3)
        grid.set_row_spacing(1)
        grid.set.margin(4)

        label1 = label = Gtk.Label(
            "(VPIP : 27%)")
        label2 = Gtk.Label(
            "(VPIP : 27%)")
        label3 = Gtk.Label(
            "(VPIP : 27%)")
        label4 = Gtk.Label(
            "(VPIP : 27%)")
        label5 = Gtk.Label(
            "(VPIP : 27%)")
        label6 = Gtk.Label(
            "(VPIP : 27%)")

        grid.attach(label1, 0 ,0 ,1,1)
        grid.attach(label2, 0, 1, 1, 1)
        grid.attach(label3, 1, 1, 1, 1)
        grid.attach(label4, 1, 0, 1, 1)
        grid.attach(label5, 2, 0, 1, 1)
        grid.attach(label6, 2, 1, 1, 1)







win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
