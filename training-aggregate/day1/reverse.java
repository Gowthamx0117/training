import java.util.Scanner;
class reverse{
    public static void main(String[] args){
        try(Scanner scanner=new Scanner(System.in)){
            int a=scanner.nextInt();
            while (a!=0){
                int d=a%10;
                System.out.println(d);
                a=a/10;
            }
        }
    }
}