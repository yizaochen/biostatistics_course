class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'(X:{self.x:.3f}, Y:{self.y:.3f})'
    
class Tree:
    def __init__(self, level_begin, level_end):
        self.level_begin = level_begin
        self.level_end = level_end
        
        self.result = self.create_container()
        
    def create_container(self):
        d_result = dict()
        for i in range(self.level_begin, self.level_end+1):
            d_result[i] = list()
        return d_result
    
    def make_level_end(self):
        n_point = 2 ** self.level_end
        for y in range(1, n_point+1):
            p = Point(self.level_end, y)
            self.result[self.level_end].append(p)
    
    def process_data(self):
        for level in range(self.level_end-1, self.level_begin-1, -1):
            self.make_data(level)
            
    def make_data(self, level):
        n_point = 2 ** level
        data_prev = self.result[level+1]
        for idx in range(n_point):
            y_down = data_prev[idx * 2].y
            y_up = data_prev[idx*2+1].y
            p = Point(level, (y_down+y_up)/2)
            self.result[level].append(p)
            
    def get_xlist_ylist_for_level(self, level):
        data = self.result[level]
        xlist = list()
        ylist = list()
        for p in data:
            xlist.append(p.x)
            ylist.append(p.y)
        return xlist, ylist

class TreeModify:
    def __init__(self):
        self.result = None

    def create_container(self, level_list):
        d_result = dict()
        for i in level_list:
            d_result[i] = list()
        self.result = d_result
        print("Set result container.")

    def make_data_by_npoints(self, n_point, level):
        for y in range(n_point):
            p = Point(level, y)
            self.result[level].append(p)

    def make_data_by_ylist(self, ylist, level):
        for y in ylist:
            p = Point(level, y)
            self.result[level].append(p)

    def make_data_by_prev_level(self, level):
        data_prev = self.result[level+1]
        n_point = int(len(data_prev) / 2)
        for idx in range(n_point):
            y_down = data_prev[idx * 2].y
            y_up = data_prev[idx*2+1].y
            p = Point(level, (y_down+y_up)/2)
            self.result[level].append(p)

    def get_xlist_ylist_for_level(self, level):
        data = self.result[level]
        xlist = list()
        ylist = list()
        for p in data:
            xlist.append(p.x)
            ylist.append(p.y)
        return xlist, ylist

    
    
def scatter_xy(ax, xlist, ylist):
    ax.scatter(xlist, ylist, s=20, color='black')