class pen:
    def use(self):
        return "Writing"
    
class eraser:
    def use(self):
        return "Erasing"
    
def perfrom_task(tool):
    print(tool.use())
perfrom_task(pen())
perfrom_task(eraser())