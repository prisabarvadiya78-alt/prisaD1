import java.util.*;
class ScannerTest
{
public static void main(String args[])
{
     Scanner sc=new Scanner(System.in);
    System.out.println("Enter your rollno:");
     int rollno=sc.nextInt();
      System.out.println("Enter your nane:");
     String name=sc.next();
   System.out.println("Enter your fees:");
     double fee=sc.nextDouble();
    System.out.println("Enter your stream:");
    String Stream=sc.next();
	System.out.println("rollno:"+rollno+"\n name"+name+"\n fees="+fee+"\n stream"+Stream);
}

}