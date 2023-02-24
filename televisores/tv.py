class TV:

	numTV=0

	def __init__(self,marca,estado):

		self.marca=marca
		self.estado=estado
		self.canal=1
		self.volumen=1
		self.precio=500
		self.numTV+=1


	def getMarca(self):
		
		return self.marca

	def getControl(self):
		
		return self.control

	def getPrecio(self):
		
		return self.precio

	def getVolumen(self):
		
		return self.volumen

	def getCanal(self):
		
		return self.canal

	def getNumTV(self):
		
		return self.numTV

	def getEstado(self):
		
		return self.estado

	def setMarca(self,marca):
		
		return self.marca

	def setControl(self,control):
		
		self.control=control

	def setPrecio(self,precio):
		
		self.precio=precio

	def setVolumen(self,volumen):

		if 0<=volumen<=7 and self.estado:
		
			self.volumen=volumen

	def setCanal(self,canal):

		if 0<=canal<=120 and self.estado:
		
			self.canal=canal

	@classmethod
	def setNumTV(cls,numTV):
		
		cls.numTV=numTV

	def turnOn(self):
		
		self.estado=True

	def turnOff(self):
		
		self.estado=False

	def canalUp(self):

		if self.canal<120 and self.estado:
		
			self.canal+=1

	def canalDown(self):

		if self.canal>0 and self.estado:
		
			self.canal-=1

	def volumenUp(self):

		if self.volumen<7 and self.estado:

			self.volumen+=1
	
	def volumenDown(self):

		if self.volumen>0 and self.estado:
		
			self.volumen-=1