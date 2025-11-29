import java.io.File; 

public class deletefile 
{
    public static void main(String[] args)
    {
        File Obj = new File("myfile.txt");
        
        // Deleting File
        if (Obj.delete()) {
            System.out.println("The deleted file is : " + Obj.getName());
        }
        else {
            System.out.println(
                "Failed in deleting the file.");
        }
    }
}