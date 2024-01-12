import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.Reader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import org.apache.ibatis.jdbc.ScriptRunner;
import java.sql.Statement;

public class Main {
    /*public static void main(String[] args) {
        System.out.println("Hello world!");
    }*/
    /*public static void forName(String className)throws ClassNotFoundException{
        Class.forName("oracle.jdbc.driver.OracleDriver");

    }*/
    public static void JDBCexample(String dbid, String userid, String passwd) throws SQLException
    {
        try (Connection conn = DriverManager.getConnection(
                "root@localhost:3306/dbmsproj", 'root', '123456789');

             Statement stmt = conn.createStatement();
        )
        {
            stmt
        }
            catch (SQLException sqle) {

        System.out.println("SQLException : " + sqle);

    }
    }
}