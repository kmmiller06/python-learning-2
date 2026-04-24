def practice_1_basic_exceptions():
    """
    Practice identifying and handling common exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 1: Handle the Exceptions")
    print("="*50)

    # TODO 1: Fix division by zero
    def safe_divide(a, b):
        """Return a/b or None if division by zero"""
        try:
            return a / b
        except ZeroDivisionError:
            return None

    # Test your function
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")

    # TODO 2: Fix list index error
    def safe_get_item(lst, index):
        """Get item at index or return 'Not found'"""
        try:
            return lst[index]
        except IndexError:
            return "Not found"

    # Test your function
    my_list = [1, 2, 3]
    print(f"Item at index 1: {safe_get_item(my_list, 1)}")
    print(f"Item at index 10: {safe_get_item(my_list, 10)}")

    # TODO 3: Handle multiple exceptions
    def convert_to_number(value):
        """Convert string to int or float, return None if impossible"""
        try:
            return int(value)
        except (ValueError, TypeError):
            try:
                return float(value)
            except (ValueError, TypeError):
                return None

    # Test conversions
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = convert_to_number(val)
        print(f"Converting '{val}': {result}")

practice_1_basic_exceptions()


def practice_2_exception_hierarchy():
    """
    Practice with exception hierarchy
    """
    print("\n" + "="*50)
    print("EXERCISE 2: Exception Hierarchy")
    print("="*50)

    # TODO 1: Catch multiple related exceptions efficiently
    def access_data(data_structure, key):
        """
        Access data[key] whether data is list or dict.
        Return None if key doesn't exist.
        """
        try:
            return data_structure[key]
        except (IndexError, KeyError, TypeError):
            return None

    # Test with different data structures
    test_list = [10, 20, 30]
    test_dict = {"a": 1, "b": 2}

    print(f"List[1]: {access_data(test_list, 1)}")
    print(f"List[10]: {access_data(test_list, 10)}")
    print(f"Dict['a']: {access_data(test_dict, 'a')}")
    print(f"Dict['z']: {access_data(test_dict, 'z')}")

    # TODO 2: Order exception handlers correctly
    def parse_value(value):
        """
        Try to parse value as int, then float, then return as string.
        """
        try:
            return int(value)
        except (ValueError, TypeError):
            try:
                return float(value)
            except (ValueError, TypeError):
                return str(value)

    # Test parsing
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = parse_value(val)
        print(f"Parsing '{val}': {result} (type: {type(result).__name__})")

practice_2_exception_hierarchy()


def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None
        try:
            file = open(filename, 'r')
        except FileNotFoundError:
            return None
        except PermissionError:
            return None
        else:
            content = file.read()
            return content.upper()
        finally:
            if file:
                file.close()

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""
            import random
            if random.choice([True, False]):
                raise RuntimeError("Failed to acquire resource")
            self.resource = "Connected"

        def release(self):
            """Release resource - must always happen."""
            self.resource = None

        def use(self):
            """Use resource - only if acquired."""
            if not self.resource:
                raise RuntimeError("Resource not acquired")

    # Test resource management
    rm = ResourceManager("Database")

    # TODO: Use try-except-else-finally to manage resource
    try:
        rm.acquire()
    except RuntimeError:
        pass
    else:
        rm.use()
    finally:
        rm.release()

practice_3_complete_pattern()


def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Invalid game move."""
        def __init__(self, position, reason):
            super().__init__(f"Position {position}: {reason}")

    class GameOverError(GameError):
        """Game has ended."""
        def __init__(self, winner):
            super().__init__(f"Winner: {winner}")

    # TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False

        def make_move(self, row, col):
            if self.game_over:
                raise GameOverError(self.current_player)
            if not (0 <= row < 3 and 0 <= col < 3):
                raise InvalidMoveError((row, col), "Out of bounds")
            if self.board[row][col] != ' ':
                raise InvalidMoveError((row, col), "Already taken")
            self.board[row][col] = self.current_player

    # Test the game
    game = TicTacToe()
    test_moves = [
        (0, 0),
        (0, 0),
        (5, 5),
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")

practice_2_custom_exceptions()


def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    print("\n" + "="*50)
    print("EXERCISE 6: Complete Error Handler")
    print("="*50)

    # TODO: Build a file processing system with proper error handling
    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []

        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            file = None
            try:
                file = open(filename, 'r')
            except FileNotFoundError:
                self.failed_files.append((filename, "Not found"))
            except PermissionError:
                self.failed_files.append((filename, "Permission denied"))
            except Exception as e:
                self.failed_files.append((filename, str(e)))
            else:
                file.read()
                self.processed_files.append(filename)
            finally:
                if file:
                    file.close()

        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            import os
            for file in os.listdir(directory):
                self.process_file(file)

        def get_report(self):
            """
            Get processing report.
            """
            return {
                "processed": self.processed_files,
                "failed": self.failed_files,
                "total_processed": len(self.processed_files),
                "total_failed": len(self.failed_files)
            }

    # Test the processor
    processor = FileProcessor()
    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
    ]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()
    print(f"Report: {report}")

practice_3_complete_system()