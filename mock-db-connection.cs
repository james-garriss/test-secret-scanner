using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;
namespace TestConnectionString
{
    class Program
    {
        static void Main(string[] args)
        {
            using (SqlConnection conn = new SqlConnection("Server=localhost;Database=SQLShackDemo;User Id=SuperHero;Password=1pass;"))
            {
                conn.Open();
                Console.WriteLine("Connection is just opened");
                System.Threading.Thread.Sleep(10000);
                conn.Close();
            }
        }
    }
 
}