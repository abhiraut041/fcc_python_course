class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        res = f'{self.__class__.__name__}(width={self.width}, height={self.height})'
        return res
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*(self.width + self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return 'Too big for picture.'
        pic = ''
        for r in range(self.height):
            for c in range(self.width):
                pic += '*'
            pic += '\n'
        return pic
    
    def get_amount_inside(self, shape):
        a, b = self.width, self.height
        x, y = shape.width, shape.height

        if a < x or b < y:
            return 0
        
        # find how many will fit in row and col
        row_cnt = a//x
        col_cnt = b//y

        return row_cnt*col_cnt

        

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def __str__(self):
        res = f'{self.__class__.__name__}(side={self.width})'
        return res

    def set_side(self, side):
        self._set_side_helper(side)
    
    def set_width(self, side):
        self._set_side_helper(side)
    
    def set_height(self, side):
        self._set_side_helper(side)
    
    def _set_side_helper(self, side):
        self.width = side
        self.height = side



# r = Rectangle(5, 10)
# s = Square(5)

# print(r.get_amount_inside(s))

