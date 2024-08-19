namespace CSharp;

public class FizzBuzz
{
    public static void Main()
    {
        Console.WriteLine("Enter an integer: ");
        int number = Convert.ToInt32(Console.ReadLine());

        if (number % 3 == 0 && number % 5 == 0)
        {
            Console.WriteLine("FizzBuzz");
        }
        else if (number % 3 == 0)
        {
            Console.WriteLine("Fizz");
        }
        else if (number % 5 == 0)
        {
            Console.WriteLine("Buzz");
        }
        else
        {
            Console.WriteLine("Not applicable");
        }
    }
   
}