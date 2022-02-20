using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DataAccessLayer
{
    public class AuthorsDAL
    {
        private readonly IConfiguration _configuration;
        public DateTime date { get;set; }

        public AuthorsDAL(IConfiguration configuration)
        {
            _configuration = configuration;
        }

        public string GetConnectionStringFromSettings(string conn)
        {
            return _configuration.GetConnectionString(conn);
        }

        //public int InsertNewAuthor(string tableName)
        //{
        //    string query = @"INSERT INTO {tableName} "
        //}

        public JsonResult GetAuthors(string connectionstring)
        {
            string query = @"select * from authors";

            DataTable dataTable = new();
            //string sqldatasource = _configuration
            SqlDataReader sqlDataReader;


        }
    }
}
