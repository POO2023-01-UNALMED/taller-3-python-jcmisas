class Control:

	def enlazar(self,tv):
		
		self.tv=tv 
		self.tv.control=self

	def getTv(self):
		
		return self.tv

	def setTV(self,tv):
		
		self.tv=tv

	def turnOn(self):
		
		self.tv.turnOn()

	def turnOff(self):
		
		self.tv.turnOff()

	def canalUp(self):
			
		self.tv.canalUp()

	def canalDown(self):
		
		self.tv.canalDown()

	def volumenUp(self):
		
		self.tv.volumenUp()

	def volumenDown(self):
		
		self.tv.canalDown()

	def setCanal(self,canal):
		
		self.tv.setCanal(canal)