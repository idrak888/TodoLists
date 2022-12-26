full_list = [[], [], []]

def add_to_list(to_do_list):
    '''
    Adds items to a to-do list.
    :param to_do_list: the list to add to
    :return: None
    '''
    print("Here is the list: ")
    print("")

    if len(to_do_list) == 0:
        print("The list is empty.")
    else:
        for i in to_do_list:
            print(i)

    print("")
    item = input("What would you like to add? ")
    to_do_list.append(item)

    enterItems = True
    while enterItems:
        item = input("What else would you like to add to the list? (Press Enter/Return to stop) ").strip()
        if item == "":
            enterItems = False
        else:
            to_do_list.append(item)

    print("")
    print("Here is the list with your new items: ")
    print("")

    for i in to_do_list:
        print(i)


def completed_item(to_do_list):
    '''
    Mark an item from a to-do list as completed.
    :param to_do_list: the list that contains the item that was completed
    :return: None
    '''

    print("This is the chosen list: ")
    print("")

    for i in to_do_list:
        print(i)

    running = True
    while running:
        itemToMark = input("Which item do you wish to mark as complete? [Enter/Return when done] ").strip()

        if itemToMark == "":
            running = False
        elif itemToMark.lower() in (item.lower() for item in to_do_list):
            index = to_do_list.index(itemToMark.title())
            to_do_list[index] = "[x]" + to_do_list[index]

            print("")
            print("This is the list after marking the item as complete: ")

            for i in to_do_list:
                print(i)
        else:
            print("The item was not marked.")


def create_to_do_list(list_name, full_list):
    '''
    Creates a new to-do list from a file or through user input.
    :param list_name: the to-do list's name: Today, Someday, Completed
    :param full_list: the list of to-do lists
    :return: None
    '''
    method = input("Are you creating this list from a file or manually?").lower()
    todo_list = []
    if method == "file":
        filename = input("Which file are you creating the list from? ")
        f = open(filename, "r")
        print("")
        for x in f:
            item = x.replace("\n", "")
            todo_list.append(item)
            print(item)
        print("")
        print("Thank you for creating a list")
    elif method == "manually":
        add_to_list(todo_list)
        print("Thank you for creating a list")
    else:
        print("Sorry. We can't create a list that way.")

    if list_name.lower() == "today":
        full_list[0] = todo_list
    elif list_name.lower() == "someday":
        full_list[1] = todo_list
    elif list_name.lower() == "completed":
        full_list[2] = todo_list
    else:
        full_list.append(todo_list)


def edit_to_do_list(to_do_list):
    '''
    Edits items in a to-do list.
    :param to_do_list: the list to edit
    :return: None
    '''
    print("Here is the list you would like to edit: ")
    for i in to_do_list:
        print(i)

    running = True
    while running:
        original = input("Which item would you like to edit? [Enter/Return when done] ").strip()

        if original == "":
            running = False
        elif original in to_do_list:
            new = input("What would you like to change this item to? ")
            index = to_do_list.index(original)
            to_do_list[index] = new
        else:
            print("The item was not marked.")


def print_lists(all_lists):
    '''
    Prints all of the to-do lists, using different characters to delineate each list.
    :param all_lists: a list containing the Today, Someday, and Completed Lists
    :return: None
    '''

    if len(all_lists[0]) > 0:
        print(40*"#")
        print("TO-DO TODAY: \n")
        for i in all_lists[0]:
            print("    " +i)
        print(40*"#")

    if len(all_lists[1]) > 0:
        print(40*"+")
        print("TO-DO SOMEDAY: \n")
        for i in all_lists[1]:
            print("    " +i)
        print(40 * "+")

    if len(all_lists[2]) > 0:
        print(40*"x")
        print("TO-DO COMPLETED: \n")
        for i in all_lists[2]:
            print("    " +i)
        print(40*"x")


def prioritize_item(to_do_list):
    '''
    Mark an item in a to-do list as having either a high or low priority.
    :param to_do_list: the to-do list holding the item to be marked with a priority level
    :return: None
    '''
    print("This is the current list: ")
    for i in to_do_list:
        print(i)

    running = True
    while running:
        item = input("Which item would you like to prioritize? ").strip()

        if item == "":
            running = False
        elif item in to_do_list:
            index = to_do_list.index(item)

            level = input("Which level of priority? [Options: High, Low] ").lower()

            if level == "high":
                to_do_list[index] = to_do_list[index] + "!!"
            else:
                to_do_list[index] = to_do_list[index] + "--"
        else:
            print("Item not found on the list.")

    print("This is your prioritized list: ")
    for i in to_do_list:
        print(i)


def remove_completed(full_list):
    '''
    Removes any items that have been marked as completed in any to-do list, counting
    how many items are removed from each to-do list. It adds all of the removed items
    to the Completed list, removing the [x] from the item before adding it.
    :param full_list: a list containing the Today, Someday, and Completed Lists
    :return: a list containing how many items were removed from each list
    '''
    removed_from_today = 0
    removed_from_someday = 0

    for i in full_list[0]:
        if i[0:3] == "[x]":
            new = i[3:]
            full_list[2].append(new)
            full_list[0].remove(i)
            removed_from_today += 1

    for i in full_list[1]:
        if i[0:3] == "[x]":
            new = i[3:]
            full_list[2].append(new)
            full_list[1].remove(i)
            removed_from_someday += 1

    return [removed_from_today, removed_from_someday]



def sort_list(to_do_list):
    '''
    Sort a to-do list, considering priority and completion when ordering.
    :param to_do_list: the to-do list to be sorted
    :return: None
    '''
    high_priority = []
    incomplete = []
    low_priority = []
    completed = []

    for i in to_do_list:
        if i[0:3] == "[x]":
            completed.append(i)
        elif i[len(i) - 2:] == "!!":
            high_priority.append(i)
        elif i[len(i) - 2:] == "--":
            low_priority.append(i)
        else:
            incomplete.append(i)

    list_index = full_list.index(to_do_list)
    to_do_list = [] + high_priority + incomplete + low_priority + completed
    full_list[list_index] = to_do_list


def validate_option(option):
    '''
    Checks if the user has entered a valid choice. If it is invalid,
    loop until it is valid or 'done'.
    :param option: the user's choice (a string)
    :return: True, if valid
             False, if done
    '''
    if option == "add" or option == "completed" or option == "create" or option == "edit" or option == "export" or option == "prioritize" or option == "remove" or option == "sort" or option == "view":
        return True
    elif option == "done":
        return False
    else:
        print("That input is invalid. Please try again.")
        return True


def which_list(list_name, full_list):
    '''
    Checks the to-do list's name, and returns the corresponding list.
    :param list_name: the name of the list being looked for
    :param full_list: a list containing the Today, Someday, and Completed Lists
    :return: the Today, Someday, Complete, or All lists
             None, otherwise
    '''
    # index 0 of full_list --> Today list
    # index 1 of full_list --> Someday list
    # index 2 of full_list --> Completed list

    if list_name == "today":
        return full_list[0]
    elif list_name == "someday":
        return  full_list[1]
    elif list_name == "completed":
        return full_list[2]
    elif list_name == "all":
        return full_list


def write_to_file(to_do_list):
    '''
    Exports a to-do list to a file.
    :param to_do_list: the list to be exported
    :return: None
    '''

    file = input("What file would you like to write to?\n")
    write_file = open(file, 'w')

    # write to file in such a way that last line doesn't include newline character
    for item in to_do_list:
        if to_do_list.index(item) == len(to_do_list) - 1:
            write_file.write(item)
        else:
            write_file.write(item + '\n')
    write_file.close()


def main():
    '''
    Runs a program for creating, modifying, and exporting to-do lists.
    :return: None
    '''
    listName = input("Choose a list to create [Options: Today or Someday]: ").lower()
    create_to_do_list(listName, full_list)
    removedItems = []

    running = True
    while running:
        option = input("What would you like to do? [Options: add, completed, create, done, edit, export, prioritize, remove, sort, view] ")
        if validate_option(option):
            if option == "add":
                listName = input("Which list would you like to add to? [Options: Today or Someday]: ").lower()
                add_to_list(which_list(listName, full_list))
            elif option == "completed":
                listName = input("Which list would you like to complete items for? [Options: Today or Someday]: ").lower()
                completed_item(which_list(listName, full_list))
            elif option == "create":
                listName = input("Name of list to create: ").lower()
                create_to_do_list(listName, full_list)
            elif option == "edit":
                listName = input("Name of list to edit: ").lower()
                edit_to_do_list(which_list(listName, full_list))
            elif option == "export":
                listName = input("Which list would you like to export? [Options: Today, Someday, Completed]: ").lower()
                write_to_file(which_list(listName, full_list))
            elif option == "prioritize":
                listName = input("Name of list to prioritize items from: ").lower()
                prioritize_item(which_list(listName, full_list))
            elif option == "remove":
                removedItems = remove_completed(full_list)
                print(f"{removedItems[0]} removed from #Today# list and {removedItems[1]} removed from +Someday+ list.")
            elif option == "sort":
                listName = input("Name of list to sort: ").lower()
                removedItems = []
                sort_list(which_list(listName, full_list))
            elif option == "view":
                listName = input("Name of list to view [Options: Today, Someday, Completed, All]: ").lower()
                if listName == "today":
                    print_lists([which_list(listName, full_list), [], []])
                elif listName == "someday":
                    print_lists([[], which_list(listName, full_list), []])
                elif listName == "completed":
                    print_lists([[], [], which_list(listName, full_list)])
                elif listName == "all":
                    print_lists(which_list(listName, full_list))
        else:
            print_lists(full_list)
            if len(removedItems) > 0:
                print(f"{removedItems[0]} removed from #Today# list.")
                print(f"{removedItems[1]} removed from +Someday+ list.")
            running = False

main()