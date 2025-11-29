import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.FileNotFoundException;
public class BinaryFileCopy {
    public static void main(String[] args) {
        String sourceFilePath = "source.bin"; // Replace with your source file path
        String destinationFilePath = "destination.bin"; // Replace with your destination file path
        FileInputStream fis = null;
        FileOutputStream fos = null;
        try {
            fis = new FileInputStream(sourceFilePath);
            fos = new FileOutputStream(destinationFilePath);
            byte[] buffer = new byte[4096]; // Buffer for reading/writing in chunks
            int bytesRead;
            while ((bytesRead = fis.read(buffer)) != -1) {
                fos.write(buffer, 0, bytesRead);
            }
            System.out.println("Binary file copied successfully from " + sourceFilePath + " to " + destinationFilePath);
        } catch (FileNotFoundException e) {
            System.err.println("Error: One of the files was not found. " + e.getMessage());
        } catch (IOException e) {
            System.err.println("Error during file I/O operations: " + e.getMessage());
        } finally {
            try {
                if (fis != null) {
                    fis.close();
                }
                if (fos != null) {
                    fos.close();
                }
            } catch (IOException e) {
                System.err.println("Error closing streams: " + e.getMessage());
            }
        }
    }
}