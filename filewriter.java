import java.io.FileWriter;
import java.io.IOException; 

public class filewriter 
{
    public static void main(String[] args)
    {
        // Writing Text File       
        try {

            FileWriter Writer = new FileWriter("myfile.txt");

            // Writing File
            Writer.write("Back Pakki haii !!!");
            Writer.close();
            
            System.out.println("Successfully written.");
        }

        // Exception Thrown
        catch (IOException e) {
            System.out.println("An error has occurred.");
            e.printStackTrace();
        }
    }
}