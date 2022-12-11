class Monkey:
    def __init__(self, monkey_items: list(list()), monkey_index: int, items: list(), 
                 worry_operator: str, worry_value: int, test_against: int, lcm: int, 
                 true_target: int, false_target: int) -> None:
        self.monkey_items = monkey_items
        self.monkey_index = monkey_index
        self.items = items
        self.monkey_items.append(self.items)
        if worry_operator == "add":
            if worry_value != 0:
                self.operation = lambda x: x + worry_value
            else:
                self.operation = lambda x: x + x
        elif worry_operator == "times":
            if worry_value != 0:
                self.operation = lambda x: x * worry_value
            else:
                self.operation = lambda x: x * x
        self.test_against = test_against
        self.lcm = lcm
        self.true_target = true_target
        self.false_target = false_target
        self.items_inspected = 0
    
    def inspect(self) -> None:
        for item in self.items.copy():
            item_index = self.items.index(item)
            item = self.operation(item)
            # item = item // 3          # Part One
            item = item % self.lcm
            if item % self.test_against == 0:
                self.throw_to(item_index, item, self.true_target)
            else:
                self.throw_to(item_index, item, self.false_target)
            self.items_inspected += 1
        
    
    def throw_to(self, remove_index: int, item: int, target: int) -> None:
        self.items.pop(remove_index)
        self.monkey_items[target].append(item)
        pass
        