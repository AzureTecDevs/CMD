import PySimpleGUI as sg
import ext


cont = sg.UserSettings()
rootnodes = cont['_USERS_']

class Tree_Data(sg.TreeData):

    def __init__(self):
        super().__init__()

    def move(self, key1, key2):
        if key1 == '':
            return False
        node = self.tree_dict[key1]
        parent1_node = self.tree_dict[node.parent]
        parent1_node.children.remove(node)
        parent2_node = self.tree_dict[key2]
        parent2_node.children.append(node)
        return True

    def delete(self, key):
        if key == '':
            return False
        node = self.tree_dict[key]
        key_list = [key, ]
        parent_node = self.tree_dict[node.parent]
        parent_node.children.remove(node)
        while key_list != []:
            temp = []
            for item in key_list:
                temp += self.tree_dict[item].children
                del self.tree_dict[item]
            key_list = temp
        return True

treedata = Tree_Data()
#rootnodes=[
#   ["","AzureTecDevs", "AzureTecDevs", 'azuretecdevs@gmail.com']
#]
for row in rootnodes:
   treedata.Insert( row[0], row[1], row[2], row[3:])
tree=sg.Tree(data=treedata,
   headings=['E-Mail'],
   auto_size_columns=False,
   select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
   num_rows=10,
   col0_width=3,
   key='-TREE-',
   show_expanded=False,
   enable_events=True,
   expand_x=True,
   expand_y=True,
)
menu = [ ['Window', ['Exit', 'About'] ], ['Contacts', ['New', 'Delete']] ]
layout=[[sg.Menu(menu)],[tree]]
window=sg.Window("Contacts", layout, size=(600, 600), resizable=True)

while True:
   event, values = window.read(timeout=10)
   #print ("event:",event, "values:",values)
   if event in (sg.WIN_CLOSED, 'Exit'):
      break
   if event == 'About':
      sg.popup('Description: Contacts List\nAuthor: AzureTecDevs\nVersion: v1.1.8', title='Contacts - About')
   if event == 'New':
      name = sg.popup_get_text('Name/Username', title='Contacts - New')
      email = sg.popup_get_text('E-Mail', title='Contacts - New')
      treedata.Insert('', name, name, email)
      new = ['', name, name, email]
      cont['_USERS_'].append(new)
      #print(cont['_USERS_'])
      window['-TREE-'].update(treedata)
      window.refresh()
   if event == 'Delete':
      name = sg.popup_get_text('Name/Username', title='Contacts - Delete')
      treedata.delete(name)
      window['-TREE-'].update(treedata)
      window.refresh()