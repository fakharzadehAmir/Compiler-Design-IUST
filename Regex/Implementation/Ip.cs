global using NUnit.Framework;
using System.Text.RegularExpressions;
namespace Assignment1;

public class IpAddresses
{ 
    public string CheckAddress(string input) {
         var ipv4 = new Regex(@"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$");
         var ipv6 = new Regex(@"^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$");
         if (ipv4.IsMatch(input))
             return "this is IPv4";
         else if (ipv6.IsMatch(input))
             return "this is IPv6";
         return "this is not IP";
    }    
}