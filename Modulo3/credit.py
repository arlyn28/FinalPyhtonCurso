import java.util.Scanner
class Tarjeta_de_credito:
        Scanner_entrada = new_Scanner(System.in)
        int(tarjeta)
        System.out.println("Introduzca los 4 primeros digitos de su tarjeta: ");
        tarjeta = entrada.nextInt()
        if (tarjeta >= 510 & tarjeta <= 559):
            print("La tarjeta es Mastercard")
        elif (tarjeta >= 4000 & tarjeta <= 4999):
            print("La tarjeta es visa")
        elif (tarjeta >= 3400 & tarjeta <= 3799):
            print("La tarjeta es american express")
        elif (tarjeta >= 3000 & tarjeta <= 3059):
            print("La tarjeta es diners club")
        elif (tarjeta >= 4000 & tarjeta <= 4999):
            print("La tarjeta es visa")
        elif (tarjeta == 6011):
            print("La tarjeta es discover")
        elif (tarjeta == 6520):
            print("La tarjeta es palacio del hierro")
        
            
        
        String_numero= entrada.nextLine()
        print("Ahora introduzca su tarjeta hasta el penultimo numero sin espacios ni guiones")
        numero = entrada.nextLine()
        print(luhnTest(numero))
static boolean luhnTest(String numero)

int s1 = 0, s2 = 0
String_reversa = new StringBuffer(numero).reverse().toString()
for(int i = 0 ;i < reversa.length();i++){
            int digito = Character.digit(reversa.charAt(i), 10);
            if (i % 2 == 0)
            {//this is for odd digits, they are 1-indexed in the algorithm
                s1 += digito;
            else:
                //add 2 * digit for 0-4, add 2 * digit - 9 for 5-9
                s2 += 2 * digito;
                if(digito >= 5)
                    s2 -= 9;
                
                    
        print("La tarjeta es:")
return (s1 + s2) % 10 == 0