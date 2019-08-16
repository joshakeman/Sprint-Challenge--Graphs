def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        found = []

        while s.size() > 0:
            current = s.pop()

            if current not in found:
                found.append(current)
                for next_vert in self.vertices[current]:
                    s.push(next_vert)
        
        print(f'DFT: {found}')