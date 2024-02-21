namespace Assignment1.Tests
{
    public class Question2
    {
        [Test]
        public void IpTest()
        {
            var checkFunction = new IpAddresses();
            Assert.Multiple(() =>
            {
                Assert.That(checkFunction.CheckAddress("192.168.1.1"), Is.EqualTo("this is IPv4"));
                Assert.That(checkFunction.CheckAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334"), Is.EqualTo("this is IPv6"));
                Assert.That(checkFunction.CheckAddress("invalid"), Is.EqualTo("this is not IP"));
                Assert.That(checkFunction.CheckAddress("10.0.0.255"), Is.EqualTo("this is IPv4"));
                Assert.That(checkFunction.CheckAddress("300.200.100.50"), Is.EqualTo("this is not IP"));
                Assert.That(checkFunction.CheckAddress("abcd"), Is.EqualTo("this is not IP"));
                Assert.That(checkFunction.CheckAddress("0:0:0:0:0:0:0:1"), Is.EqualTo("this is IPv6"));
                Assert.That(checkFunction.CheckAddress("255.255.255.255"), Is.EqualTo("this is IPv4"));
            });
        }
    }
}