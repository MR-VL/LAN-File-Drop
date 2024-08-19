namespace CSharp;

public class Temperature
{
    public static void Main()
    {
        string original = "", converted = "";
        double convertedTemp = 0;
        Console.WriteLine("Enter a temperature: ");
        var temperature = Convert.ToDouble( Console.ReadLine());
       
        Console.WriteLine("Enter 'F' to convert from Fahrenheit to Celsius\nOr 'C' to convert from Celsius to Fahrenheit");
        char choice = Convert.ToChar(Console.ReadLine());

        if (choice == 'f' || choice == 'F')
        {
            original = "Fahrenheit";
            converted = "Celsius";
            convertedTemp = fahrenheit(temperature);
        }
        else if (choice == 'c' || choice == 'C')
        {
            original = "Celsius";
            converted = "Fahrenheit";
            convertedTemp = celsius(temperature);
        }
       
        System.Console.WriteLine(temperature + " "+ original + " = " + convertedTemp + " " + converted);
        
        
    }

    private static double fahrenheit(double temp)
    {
        return (temp - 32) * 5/9;
    }

    private static double celsius(double temp)
    {
        return (temp * (9 / 5)) + 32;
    }
}