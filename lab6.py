from typing import Any, List, Union, Callable, Dict

class TreeNode:
    """
    Klasa odpowiedzialna za węzeł drzewa (Zadanie 5.1 A)
    """
    value: Any
    children: List["TreeNode"]

    def __init__(self, value: Any, children: List["TreeNode"] = None):
        self.value = value
        self.children = children if children is not None else []

    def __str__(self):
        # (a) funkcja __str__ zwraca value
        return str(self.value)

    def is_leaf(self) -> bool:
        # (b) sprawdzi czy węzeł jest liściem (brak dzieci)
        return len(self.children) == 0

    def add(self, child: "TreeNode") -> None:
        # (c) doda węzeł przyjęty w argumencie jako dziecko
        self.children.append(child)

    def for_each_deep_first_rec(self, visit: Callable[["TreeNode"], None]) -> None:
        # (d) DFS rekurencyjnie
        visit(self)  # odwiedź bieżący
        for child in self.children:
            child.for_each_deep_first_rec(visit)

    def for_each_breadth_first(self, visit: Callable[["TreeNode"], None]) -> None:
        # (e) BFS (Level Order) przy użyciu kolejki FIFO
        queue = [self]  # używamy listy jako kolejki
        
        while len(queue) > 0:
            current_node = queue.pop(0)  # pobierz pierwszy element
            visit(current_node)          # odwiedź
            # dodaj dzieci do kolejki
            for child in current_node.children:
                queue.append(child)

    def for_each_deep_first(self, visit: Callable[["TreeNode"], None]) -> None:
        # (f) DFS nierekurencyjnie (z użyciem stosu LIFO)
        stack = [self]
        
        while len(stack) > 0:
            current_node = stack.pop() # pobierz ostatni element (LIFO)
            visit(current_node)
            
            # Dodajemy dzieci na stos w odwrotnej kolejności, 
            # aby przy zdejmowaniu (pop) zachować kolejność od lewej do prawej
            for child in reversed(current_node.children):
                stack.append(child)

    def search(self, value: Any) -> Union["TreeNode", None]:
        # (g) sprawdzi czy węzeł lub dzieci zawierają wartość
        # Wykorzystuję logikę DFS do przeszukania
        if self.value == value:
            return self
        
        for child in self.children:
            found = child.search(value)
            if found:
                return found
        return None

    def node_to_nested_dict(self) -> dict:
        # (h) przekształca na zagnieżdżony słownik
        # Format: {self.value: {child1_val: {...}, child2_val: {...}}}
        children_dict = {}
        for child in self.children:
            children_dict.update(child.node_to_nested_dict())
        
        return {self.value: children_dict}


class Tree:
    """
    Klasa odpowiedzialna za przechowywanie całej struktury drzewa (Zadanie 5.1 B)
    """
    root: TreeNode

    def __init__(self):
        self.root = None

    def add(self, value: Any, parent_value: Any) -> None:
        # (a) dodaje nowe dziecko z value do rodzica o parent_value
        if self.root is None:
            # Jeśli drzewo jest puste, pierwszy dodany element staje się korzeniem
            # (Uwaga: w typowym użyciu z zadania ustawiamy root ręcznie, 
            # ale tutaj obsłużymy przypadek inicjalizacji jeśli parent_value nie istnieje)
             self.root = TreeNode(value)
             return

        parent_node = self.root.search(parent_value)
        if parent_node:
            parent_node.add(TreeNode(value))
        else:
            # Opcjonalnie: rzuć błąd lub obsłuż przypadek braku rodzica
            print(f"Nie znaleziono rodzica o wartości: {parent_value}")

    def for_each_deep_first_rec(self, visit: Callable[["TreeNode"], None]) -> None:
        # (b) DFS od korzenia
        if self.root:
            self.root.for_each_deep_first_rec(visit)

    def for_each_breadth_first(self, visit: Callable[["TreeNode"], None]) -> None:
        # (c) BFS od korzenia
        if self.root:
            self.root.for_each_breadth_first(visit)

    def tree_to_nested_dict(self) -> dict:
        # (e) drzewo na zagnieżdżony słownik
        if self.root:
            return self.root.node_to_nested_dict()
        return {}

    def tree_to_dict(self) -> dict:
        # (f) drzewo na słownik płaski value: [children_values]
        # Podpowiedź: użyj BFS
        if not self.root:
            return {}
        
        result_dict = {}
        
        def visitor(node):
            result_dict[node.value] = [child.value for child in node.children]
            
        self.for_each_breadth_first(visitor)
        return result_dict

    def dict_to_tree(self, d: dict) -> None:
        # (g) przekształca słownik na drzewo
        # Uwaga: zerowy klucz słownika jest korzeniem
        if not d:
            return

        # Pobranie pierwszego klucza (korzeń)
        iterator = iter(d)
        root_val = next(iterator)
        
        self.root = TreeNode(root_val)
        
        # Kolejka do przetwarzania (tak jak BFS), aby budować drzewo warstwami
        # Lub prościej: iterujemy po słowniku i dodajemy dzieci, 
        # zakładając że rodzice są już w drzewie (co gwarantuje BFS przy tworzeniu słownika)
        
        # Iterujemy po całym słowniku i dodajemy relacje
        # Ponieważ metoda add w klasie Tree wyszukuje rodzica (search),
        # możemy po prostu przejść po słowniku.
        
        # Najpierw dodajemy dzieci korzenia, potem dzieci dzieci itd.
        # Aby mieć pewność, że rodzic istnieje przed dodaniem dziecka,
        # przydałaby się kolejka, ale metoda 'add' z zadania używa 'search',
        # więc kolejność słownika ma znaczenie tylko dla wydajności.
        # Zakładamy, że słownik wejściowy jest posortowany topologicznie (np. z BFS).
        
        for parent_val, children_list in d.items():
            # Upewnij się, że rodzic istnieje (dla korzenia już stworzyliśmy)
            # Jeśli to korzeń, tylko dodajemy jego dzieci
            for child_val in children_list:
                self.add(child_val, parent_val)


# --- TESTY (Zgodne z sekcją Testy w PDF) ---

if __name__ == "__main__":
    print("--- Rozpoczynam Testy ---")

    # (a) Węzły:
    node0 = TreeNode("F")
    
    assert node0.value == "F"
    assert node0.children == []
    assert str(node0) == "F"
    assert node0.is_leaf() == True
    assert node0.node_to_nested_dict() == {"F": {}}
    
    # Tworzenie struktury testowej ręcznie
    # node1 ma dzieci A i D
    node1 = TreeNode("B", [TreeNode("A"), TreeNode("D")])
    node2 = TreeNode("G")
    
    assert node2.children == []
    assert node1.children[0].value == "A"
    
    node0.add(node1)
    node0.add(node2)
    
    assert node0.children == [node1, node2]
    assert node2.children == []
    
    # Test DFS Rekurencyjny
    l_deep_rec = []
    node0.for_each_deep_first_rec(lambda n: l_deep_rec.append(n))
    # Oczekiwane: F -> B -> A -> D -> G
    assert [x.value for x in l_deep_rec] == ["F", "B", "A", "D", "G"]
    
    # Test DFS Iteracyjny (dodatkowy z gwiazdką)
    l_deep_iter = []
    node0.for_each_deep_first(lambda n: l_deep_iter.append(n))
    assert [x.value for x in l_deep_iter] == ["F", "B", "A", "D", "G"]

    # Test BFS
    l_breadth = []
    node0.for_each_breadth_first(lambda n: l_breadth.append(n))
    # Oczekiwane: F -> B -> G -> A -> D
    assert [x.value for x in l_breadth] == ["F", "B", "G", "A", "D"]
    
    # Test Search
    assert node0.search("G") == node2
    assert node1.search("G") is None
    
    # Test Nested Dict
    # Oczekiwane: F ma dzieci B (z A, D) i G (puste)
    expected_nested = {"F": {"B": {"A": {}, "D": {}}, "G": {}}}
    assert node0.node_to_nested_dict() == expected_nested
    
    print("Testy sekcji (a) - Węzły: ZALICZONE")

    # (b) Drzewo:
    tree_ = Tree()
    assert tree_.root is None
    
    # Ustawiamy korzeń na node0 z poprzedniego testu (F -> B, G...)
    # Uwaga: node0 ma już strukturę F->(B->(A,D), G)
    # W PDF w sekcji testy (b) jest: tree_.add("C", "D") itd.
    # Musimy upewnić się, że struktura jest taka jak na rysunku w PDF
    # Rysunek: F -> B, G; B -> A, D; D -> C, E; G -> I; I -> H
    
    tree_.root = node0 
    
    # Dodajemy resztę węzłów zgodnie z testem w PDF
    tree_.add("C", "D") # C pod D
    tree_.add("E", "D") # E pod D
    tree_.add("I", "G") # I pod G
    tree_.add("H", "I") # H pod I
    
    # Weryfikacja DFS całego drzewa
    l_deep_tree = []
    tree_.for_each_deep_first_rec(lambda n: l_deep_tree.append(n))
    # Kolejność: F, B, A, D, C, E, G, I, H
    assert [x.value for x in l_deep_tree] == ["F", "B", "A", "D", "C", "E", "G", "I", "H"]
    
    # Weryfikacja BFS całego drzewa
    l_breadth_tree = []
    tree_.for_each_breadth_first(lambda n: l_breadth_tree.append(n))
    # Kolejność warstwami: F -> B, G -> A, D, I -> C, E, H
    assert [x.value for x in l_breadth_tree] == ["F", "B", "G", "A", "D", "I", "C", "E", "H"]
    
    # Tree to Dict
    d = tree_.tree_to_dict()
    expected_d = {
        "F": ["B", "G"], 
        "B": ["A", "D"],
        "G": ["I"],
        "A": [],
        "D": ["C", "E"], 
        "I": ["H"],
        "C": [], 
        "E": [], 
        "H": []
    }
    # Porównanie słowników (kolejność kluczy może być inna, ale zawartość ta sama)
    assert d == expected_d
    
    # Tree to Nested Dict
    d1 = tree_.tree_to_nested_dict()
    expected_d1 = {
        "F": {
            "B": {
                "A": {}, 
                "D": {"C": {}, "E": {}}
            }, 
            "G": {
                "I": {"H": {}}
            }
        }
    }
    assert d1 == expected_d1
    
    # Dict to Tree (Odtwarzanie drzewa)
    tree_1 = Tree()
    assert tree_1.root == None
    
    # Używamy słownika d wygenerowanego wcześniej
    tree_1.dict_to_tree(d)
    
    l_deep_tree_1 = []
    tree_1.for_each_deep_first_rec(lambda n: l_deep_tree_1.append(n))
    
    # Sprawdzenie czy odtworzone drzewo ma taką samą strukturę DFS
    assert [x.value for x in l_deep_tree_1] == ["F", "B", "A", "D", "C", "E", "G", "I", "H"]
    
    print("Testy sekcji (b) - Drzewo: ZALICZONE")
    print("WSZYSTKIE TESTY ZALICZONE POMYŚLNIE")
