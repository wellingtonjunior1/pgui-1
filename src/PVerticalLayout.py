import pgui.src.PLayout as PLayout

class new(PLayout.new):
	def __init__(self):
		PLayout.new.__init__(self)
		self.spacing = 6
	
	def apply_layout(self, control, count):
		index = control.layout_order
		height = self._prevs
		
		control.bounds[0] = self.padding[0] + self.bounds[0]
		control.bounds[1] = (index * self.spacing) + height + self.padding[1] + self.bounds[1]
		control.bounds[2] = self.bounds[2] - self.padding[2]*2
		
		if self.fit:
			pad = (self.padding[3]/count)
			control.bounds[3] = (self.bounds[3] / count) - (self.spacing+pad)
		
		self._prevs += control.bounds[3]
		PLayout.new.apply_layout(self, control, count)