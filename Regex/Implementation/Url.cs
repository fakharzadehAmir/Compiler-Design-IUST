global using NUnit.Framework;
using System.Text.RegularExpressions;
namespace Assignment1;

public class UrlChecker
{
    private const string UrlPattern = @"^(https?|ftp)://([A-Za-z0-9.-]+)(:\d+)?(/([A-Za-z0-9-]+)*/)*$";
    public bool ValidateUrl(string input) => Regex.IsMatch(input, UrlPattern);
}