objects = ['fox','chicken','corn']

class TransportState:
    def __init__(self,left,right,farmer_left,history):
        self.history=history
        self.left_bank=left
        self.right_bank=right
        self.farmer_left=farmer_left

    def is_legal(self):
        objects = self.right_bank if self.farmer_left else self.left_bank
        if 'fox' in objects:
            return 'chicken' not in objects
        if 'chicken' in objects:
            return 'corn' not in objects
        return True
    
    def is_complete(self):
        return len(self.left_bank) == 0 and len(self.right_bank) == 3
    
    def get_transitions(self):
        objects = self.left_bank if self.farmer_left else self.right_bank
        results = []
        for i in range(len(objects)+1):
            left = list(self.left_bank)
            right = list(self.right_bank)
            _from = left if self.farmer_left else right
            _to = right if self.farmer_left else left
            history = list(self.history)
            obj = None
            if i < len(objects):
                obj = objects[i]
                _from.remove(obj)
                _to.append(obj)
            history.append(obj)
            tx = TransportState(left,right,not self.farmer_left,history)
            if tx.is_legal():
                results.append(tx)
        return results

init=TransportState(objects,[],True,[])
all_state = [init]

while (True):
    for state in all_state:
        next = state.get_transitions()
        for next_state in next:
            if next_state.is_complete():
                print(next_state.history)
                exit()
        all_state.extend(next)
        all_state.remove(state)
