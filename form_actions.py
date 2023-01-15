"""

empty for now, place holder to think
"""


def create_new_user(form, mongo_client) -> bool:
    """
    :param form: takes the results from the html form, this is a dictionary
    :param mongo_client: the mongo client you're interacting with
    :return: true if it created a new user, otherwise false
    """
    print('received this!')
    for thing in form:
        print(thing)

    print(form)
    return False  # for now because we're not doing anything
