
class Stack:
	"""Simple LIFO stack implementation using Python list as underlying storage.

	Methods:
	- push(item): push an item on top of the stack
	- pop(): remove and return the top item; returns None if stack is empty
	- peek(): return the top item without removing it; returns None if empty
	- is_empty(): True when stack has no items
	- size(): number of items in the stack
	"""

	def __init__(self):
		self._items = []

	def push(self, item):
		self._items.append(item)

	def pop(self):
		if not self._items:
			return None
		return self._items.pop()

	def peek(self):
		if not self._items:
			return None
		return self._items[-1]

	def is_empty(self):
		return len(self._items) == 0

	def size(self):
		return len(self._items)

	def __str__(self):
		# show stack with top at the right
		return f"Stack(bottom -> top): {self._items}"


def interactive_menu():
	s = Stack()
	print("Stack interactive demo (push/pop/peek). Enter numbers for menu choices.")

	menu = (
		"\nChoose an operation:\n"
		"1) Push an item\n"
		"2) Pop an item\n"
		"3) Peek top item\n"
		"4) Display stack\n"
		"5) Size\n"
		"6) Reset (new empty stack)\n"
		"7) Run sample testcases\n"
		"8) Exit\n"
	)

	def run_sample_tests(stack):
		print("\nRunning sample testcases:")
		seq = [10, 20, 30]
		print("Pushing:", seq)
		for x in seq:
			stack.push(x)
		print(stack)
		print("Peek ->", stack.peek())
		print("Pop ->", stack.pop())
		print(stack)
		print("Pop ->", stack.pop())
		print("Pop ->", stack.pop())
		print("Pop on empty ->", stack.pop())
		print("Final:", stack)

	while True:
		try:
			choice = input(menu + "Choice: ")
		except (EOFError, KeyboardInterrupt):
			print("\nExiting.")
			break

		choice = choice.strip()
		if not choice:
			continue

		if choice == "1":
			val = input("Enter value to push: ")
			# keep as string; user can type numbers if desired
			s.push(val)
			print("Pushed.")
		elif choice == "2":
			popped = s.pop()
			if popped is None:
				print("Stack is empty. Nothing to pop.")
			else:
				print(f"Popped: {popped}")
		elif choice == "3":
			top = s.peek()
			if top is None:
				print("Stack is empty.")
			else:
				print(f"Top item: {top}")
		elif choice == "4":
			print(s)
		elif choice == "5":
			print("Size:", s.size())
		elif choice == "6":
			s = Stack()
			print("Stack reset to empty.")
		elif choice == "7":
			run_sample_tests(s)
		elif choice == "8":
			print("Goodbye.")
			break
		else:
			print("Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
	interactive_menu()
