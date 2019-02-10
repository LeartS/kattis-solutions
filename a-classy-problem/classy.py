
class Person(object):

    def __init__(self, name, class_):
        self.name = name
        self.class_ = class_

    def __lt__(self, other):
        return (self.name > other.name
                if self.class_ == other.class_
                else self.class_ < other.class_)

T = int(input())
for _ in range(T):
    n_people = int(input())
    people = []
    for _ in range(n_people):
        name, class_, _ = input().split()
        name = name[:-1]
        class_ = '-'.join((class_.split('-')[::-1] + ['middle'] * 10)[:10])
        people.append(Person(name, class_))
    print('\n'.join(p.name for p in sorted(people, reverse=True)))
    print('=' * 30)
