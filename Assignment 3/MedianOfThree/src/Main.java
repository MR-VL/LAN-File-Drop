import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static int comparisons = 0;
    static int medianOfThree(List<Integer> arr, int low, int high) {
        int middle = low + (high - low) / 2;

        int lower = arr.get(low);
        int middlenum = arr.get(middle);
        int upper = arr.get(high);

        if ((lower <= middlenum && middlenum <= upper) || (upper <= middlenum && middlenum <= lower)) {
            return middle;
        } else if ((middlenum <= lower && lower <= upper) || (upper <= lower && lower <= middlenum)) {
            return low;
        } else {
            return high;
        }
    }

    static int partition(List<Integer> arr, int low, int high) {
        int pivotIndex = medianOfThree(arr, low, high);
        swap(arr, pivotIndex, high);
        int pivot = arr.get(high);
        int i = low - 1;

        for (int j = low; j <= high - 1; j++) {
            comparisons++;
            if (arr.get(j) < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);
        return i + 1;
    }

    static void swap(List<Integer> arr, int i, int j) {
        int temp = arr.get(i);
        arr.set(i, arr.get(j));
        arr.set(j, temp);
    }

    static void quickSort(List<Integer> arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }
    
    public static List<Integer> readFile(String filename) {
        List<String> numbers = new ArrayList<>();
        Scanner input;
        try {
            input = new Scanner(new File(filename));
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        input.useDelimiter("[,\\s]+");

        while (input.hasNext()) {
            numbers.add(input.next().trim());
        }
        input.close();

        return convertToInt(numbers);
    }

    public static List<Integer> convertToInt(List<String> nums) {
        List<Integer> numbers = new ArrayList<>();
        for (String str : nums) {
            if (!str.isEmpty()) {
                try {
                    numbers.add(Integer.parseInt(str));
                } catch (NumberFormatException e) {
                    System.out.println("Invalid number format: " + str);
                }
            }
        }
        return numbers;
    }


    public static void main(String[] args) {
        System.out.println("Always using the median of three as pivot\n");
        List<Integer> TenNumbers = readFile("test_case_1-1.csv");
        List<Integer> OneHundredNumbers = readFile("test_case_2.csv");
        List<Integer> TenThousandNumbers = readFile("test_case_3.csv");

        quickSort(TenNumbers, 0, TenNumbers.size()-1);
        for (int val : TenNumbers.toArray(new Integer[0])) {
            System.out.print(val + " ");
        }

        System.out.println("\nComparisons for 10 numbers: " + comparisons);
        comparisons = 0;


        System.out.println("\n");
        quickSort(OneHundredNumbers, 0, OneHundredNumbers.size()-1);
        for (int val : OneHundredNumbers.toArray(new Integer[0])) {
            System.out.print(val + " ");
        }

        System.out.println("\nComparisons for 100 numbers: " + comparisons);
        comparisons = 0;

        System.out.println("\n");
        quickSort(TenThousandNumbers, 0, TenThousandNumbers.size()-1);
        for (int val : TenThousandNumbers.toArray(new Integer[0])) {
            System.out.print(val + " ");
        }
        System.out.println("\nComparisons for 10,000 numbers: " + comparisons);
        comparisons = 0;
    }
}
