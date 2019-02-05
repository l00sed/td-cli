class COMMANDS:
    ADD_TODO = "add_todo"
    COMPLETE_TODO = "complete_todo"
    DELETE_TODO = "delete_todo"
    EDIT_TODO = "edit_todo"
    GET_TODO = "get_todo"
    LIST_TODOS = "list_todos"
    NAME_TODO = "name_todo"
    UNCOMPLETE_TODO = "uncomplete_todo"
    ADD_GROUP = "add_group"
    DELETE_GROUP = "delete_group"
    GET_GROUP = "get_group"
    LIST_GROUPS = "list_groups"
    PRESET_GROUP = "preset_group"


class INTERACTIVE_COMMANDS:
    ADD = "add"
    DELETE = "delete"
    DOWN = "down"
    EDIT = "edit"
    ENTER = "enter"
    ESCAPE = "escape"
    QUIT = "quit"
    RECOVER = "recover"
    TOGGLE = "toggle"
    UP = "up"


class STATES:
    COMPLETED = "completed"
    UNCOMPLETED = "uncompleted"


class COMMAND_MODES:
    DEFAULT = "default"
    DELETE = "delete"
    EDIT = "edit"
