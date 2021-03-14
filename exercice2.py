
    sum=0
    class CompteBancaire:
	def __init__(self):
		self.nom="Ali"
		self.solde=1000

	
	def depot(self,sum):
		self.solde+=sum

	
 	def retrait(self,sum):
		self.solde=self.solde-sum

	
        def affiche(self):
        	print("Le solde du compte bancaire de {} est de {} euros.".format(self.nom,self.solde))
        
