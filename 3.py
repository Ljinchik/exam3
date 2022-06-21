class Tomato:
    states = {1:'Nothing',2:'Green',3:'Yellow',4:'Red'}
    def __init__(self,index):
        self._index = index
        self._state = 1
    def grow(self):
        self.next_stage()
    def is_ripe(self):
        if self._state == 4:
            return True
        else:
            return False
    def next_stage(self):
        if self._state < 4:
            self._state +=1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')
class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0,num)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self,name,plant):
        self.name = name
        self._plant = plant
    def work(self):
        print('Садовник работает')
        self._plant.grow_all()
        print('Садовник закончил работу')
    def harvest(self):
        print('Проверка зрелости')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Все плоды созрели')
        else:
            print('Не все плоды созрели')
    @staticmethod
    def knowledge_base():
        print('Помидоры лучше всего собирать красные, можно конечно и жёлтые(на подоконнике дозреют), но лучше красные, а вот зелёные лучше не трогать и подождать пока поспеют, а то можно не хило так ...')

Gardener.knowledge_base()
tomato_bush = TomatoBush(5)
gardener = Gardener('Равшан', tomato_bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()