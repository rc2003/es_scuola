#include <iostream>
using namespace std;
int main(){
	double valuta1, valuta2;
	int scelta;
	
do{
	cout << "1. Cambio DOLLARI in EURO " << endl;
	cout << "2. Cambio EURO in DOLLARI " << endl;
	cout << "3. Cambio EURO in STERLINE " << endl;
	cout << "4. Cambio STERLINE in EURO " << endl;
	cout << "5. Variazione tasso EUR/USD " << endl;
	cout << "6. Variazione tasso EUR/GBP " << endl;
	cout << "7. Uscita dal programma " << endl;
	cin >> scelta;
	
	switch(scelta){
		case(1):{ 
			cout << "Inserisci la valuta in DOLLARI -> ";
			cin >> valuta1;
			valuta2 = valuta1/1.1;
			cout << "La tua valuta in DOLLARI corrisponde a " << valuta2 << " EURO" << endl;
			
			break;
		}
		case(2):{
		cout << "Inserisci la valuta in EURO -> ";
			cin >> valuta1;
			valuta2 = valuta1*1.1;
			cout << "La tua valuta in EURO corrisponde a " << valuta2 << " DOLLARI" << endl; 
			break;
		}
		case(3):{
		cout << "Inserisci la valuta in EURO -> ";
			cin >> valuta1;
			valuta2 = valuta1*0.775;
			cout << "La tua valuta in EURO corrisponde a " << valuta2 << " STERLINE" << endl; 
			break;
		}
		case(4):{
		cout << "Inserisci la valuta in STERLINE -> ";
			cin >> valuta1;
			valuta2 = valuta1/0.775;
			cout << "La tua valuta in STERLINE corrisponde a " << valuta2 << " EURO" << endl; 
			break;
		}
		case(5):{ 
		cout << "Inserisci la valuta in EURO -> ";
			cin >> valuta1;
		cout << "Inserisci la valuta in DOLLARI -> ";
			cin >> valuta2;
		double tasso;
		tasso = valuta1/valuta2;
		cout << "Il tasso di cambio tra EURO e DOLLARI è "<< tasso << endl;	
			break;
		}
		case(6):{ 
		cout << "Inserisci la valuta in EURO -> ";
			cin >> valuta1;
		cout << "Inserisci la valuta in STERLINE -> ";
			cin >> valuta2;
		double tasso;
		tasso = valuta1/valuta2;
		cout << "Il tasso di cambio tra EURO e STERLINE è "<< tasso << endl;
			break;
		}
		case(7):{ 
			break;
		}

		}
	}while(scelta!=7);
}
