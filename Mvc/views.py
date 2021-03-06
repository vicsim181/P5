"""Script holding different classes managing the different views of the application."""
from Mvc.utils import int_input


class View:
    """Generic mclass hosting generic functions or tools used by the other classes."""
    @staticmethod
    def print_header(name, action):
        print("\n\n\n\n\n\n\n\n\n"
              "#################################################################\n"
              "#####################{:^22}".format(name), "#####################\n"
              "###########{:^42}".format(action), "###########\n"
              "#                                                               #")

    @staticmethod
    def print_middle(*args):
        for i, arg in enumerate(args):
            argument = str(i + 1) + "- " + arg
            print("#                   {:<43}".format(argument), "#")
        print("#                                                               #\n"
              "#_______________________________________________________________#")

    @staticmethod
    def print_bottom(*args):
        for arg in args:
            print("#{:^62}".format(arg), "#")

    @staticmethod
    def print_product(subtitle, product, stores):
        print("#{:^62}".format(subtitle), "#\n")
        print(f" -Name: {product.name}\n"
              f" -Quantity: {product.quantity}\n"
              f" -Nutriscore: {product.nutri_score}\n"
              f" -Ingredients: {product.ingredients}\n"
              f" -URL: {product.link_url}\n"
              f" -Store(s): {stores}\n")
        print("#                                                               #\n"
              "#_______________________________________________________________#")


class Main:
    """Class holding the view of the main menu"""
    @staticmethod
    def display_view(alt_callback, callback, callback_2, message, header_title, header_sub):
        View.print_header(header_title, header_sub)
        View.print_middle("Replace a product", "Consult my favorites")
        View.print_bottom("Press the number of your choice", "Press 0 to close")
        choice = int_input(0, 2, message)
        if choice == 0:
            alt_callback()
        elif choice == 1:
            callback()
        else:
            callback_2()


class Category:
    """Class holding the view of the categories menu"""
    @staticmethod
    def display_categories(categories, alt_callback, callback, callback_2, message, header_title, header_sub):
        View.print_header(header_title, header_sub)
        for i, category in enumerate(categories):
            argument = str(i + 1) + "- " + category.title()
            print("#                   {:<43}".format(argument), "#")
        print("#                                                               #\n"
              "#_______________________________________________________________#")
        View.print_bottom("Press the number of your choice", f"Press {i+2} to go back to Main Menu",
                          "Press 0 to close")
        choice = int_input(0, (i + 2), message)
        if choice == 0:
            alt_callback()
        elif choice in range(1, i+2):
            callback(categories[choice-1])
        else:
            callback_2()


class Product:
    """Class holding the view of the different products menus"""
    @staticmethod
    def display_products(category_name, category_id, product, i, stores, alt_callback, callback, callback_2,
                         callback_3, replaced_product, message, max_products, header_sub):
        View.print_header(category_name, header_sub)
        subtitle = f"Product n°{str(i + 1)} / {str(max_products)}"
        View.print_product(subtitle, product, stores)
        View.print_bottom("Press 1 to select this product", "To display the next product press 2",
                          "To go back to the previous product press 3", "Press 4 to go back to Main Menu",
                          "Press 0 to close")
        choice = int_input(0, 4, message)
        if choice == 0:
            alt_callback()
        elif choice == 1:
            callback(product, category_id, category_name)
        elif choice == 2:
            if i+1 == max_products:
                callback_2(category_id, category_name, i)
            callback_2(category_id, category_name, i + 1)
        elif choice == 3:
            if i == 0:
                callback_2(category_id, category_name, i)
            else:
                callback_2(category_id, category_name, i - 1)
        else:
            callback_3()

    @staticmethod
    def display_suggestions(product, i, stores, alt_callback, callback, callback_2, callback_3, replaced_product,
                            message, max_alter, header_title, header_sub):
        View.print_header(header_title, header_sub)
        subtitle = f"Product n°{str(i + 1)} / {str(max_alter)}"
        View.print_product(subtitle, product[i], stores[i])
        View.print_bottom("Press 1 to select this product", "To display the next product press 2",
                          "To go back to the previous product press 3", "Press 4 to go back to Main Menu",
                          "Press 0 to close")
        choice = int_input(0, 4, message)
        if choice == 0:
            alt_callback()
        elif choice == 1:
            callback(product[i], replaced_product)
        elif choice == 2:
            if i+1 == max_alter:
                callback_2(product, i, stores, alt_callback, callback, callback_2, callback_3,
                           replaced_product, message, 5, header_title, header_sub)
            callback_2(product, i + 1, stores, alt_callback, callback, callback_2, callback_3,
                       replaced_product, message, 5, header_title, header_sub)
        elif choice == 3:
            if i == 0:
                callback_2(product, i, stores, alt_callback, callback, callback_2, callback_3,
                           replaced_product, message, 5, header_title, header_sub)
            else:
                callback_2(product, i - 1, stores, alt_callback, callback, callback_2, callback_3,
                           replaced_product, message, 5, header_title, header_sub)
        else:
            callback_3()


class Favorite:
    """Class holding the different views of the favorite"""
    @staticmethod
    def save_generic(alt_callback, callback, header_title, header_sub, middle_message_1, middle_message_2, message):
        View.print_header(header_title, header_sub)
        print("#{:^62}".format(middle_message_1), "#\n"
              "#{:^62}".format(middle_message_2), "#")
        print("#                                                               #\n"
              "#_______________________________________________________________#")
        View.print_bottom("Press 1 to go back to Main Menu", "Press 0 to close")
        choice = int_input(0, 1, message)
        if choice == 0:
            alt_callback()
        else:
            callback()

    @staticmethod
    def save_successful(alt_callback, callback, header_title, header_sub, middle_message_1, middle_message_2, message):
        Favorite.save_generic(alt_callback, callback, header_title, header_sub, middle_message_1, middle_message_2,
                              message)

    @staticmethod
    def save_unsuccessful(alt_callback, callback, header_title, header_sub, middle_message_1, middle_message_2,
                          message):
        Favorite.save_generic(alt_callback, callback, header_title, header_sub, middle_message_1, middle_message_2,
                              message)

    @staticmethod
    def consult(favorites, alt_callback, callback, callback_2, header_title, header_sub, message):
        try:
            View.print_header(header_title, header_sub)
            print("\n")
            for i, favorite in enumerate(favorites):
                argument = str(i + 1) + "- " + favorite[0] + " | replaced by | " + favorite[1] + " | on | " + favorite[2]
                print("{:<62}".format(argument))
            print("\n"
                  "#_______________________________________________________________#")
            View.print_bottom("To delete a particular line, press its number", f"Press {i + 3} to delete all the favorites",
                              f"To go back to Main Menu press {i + 2}", "Press 0 to close")
            choice = int_input(0, i + 3, message)
            if choice == 0:
                alt_callback()
            elif choice in range(1, i + 2):
                callback(choice)
            elif choice == (i + 3):
                callback('all')
            else:
                callback_2()
        except UnboundLocalError:
            print("#                                                               #\n"
                  "#                   No favorite for the moment                  #\n"
                  "#_______________________________________________________________#\n")
            View.print_bottom("Press 1 to go back to Main Menu", "Press 0 to close")
            choice = int_input(0, 1, message)
        if choice == 0:
            alt_callback()
        else:
            callback_2()

    @staticmethod
    def delete_all(header_title, header_sub, middle_message, bottom_1, bottom_2, message, alt_callback, callback):
        View.print_header(header_title, header_sub)
        View.print_middle(middle_message)
        View.print_bottom(bottom_1, bottom_2)
        choice = int_input(0, 1, message)
        if choice == 0:
            alt_callback()
        else:
            callback()
