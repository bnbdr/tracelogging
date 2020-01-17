using Microsoft.Diagnostics.Tracing;
using Microsoft.Diagnostics.Tracing.Session;
using System;
using System.Text;
using System.Threading.Tasks;

namespace EtwConsumer
{
    class Program
    {
        static void Main(string[] providerNames)
        {
            var sessionName = "SampleEtwConsumerSession";

            Console.WriteLine($"Creating session: '{sessionName}'");
            using (var session = new TraceEventSession(sessionName))
            {
                Console.CancelKeyPress += delegate (object sender, ConsoleCancelEventArgs e)
                {
                    Console.WriteLine("stopping");
                    session.Dispose();
                };

                session.Source.Dynamic.AddCallbackForProviderEvents((providerName, eventName) =>
                {
                    return EventFilterResponse.AcceptEvent;
                }, eventData =>
                {
                    Console.WriteLine(eventData.ToString());
                });

                foreach (var name in providerNames)
                {
                    if (name.StartsWith("{") && name.EndsWith("}"))
                    {
                        var guid = new Guid(name);
                        session.EnableProvider(guid, TraceEventLevel.Verbose);
                        Console.WriteLine($"enabled {guid}");
                    }
                    else
                    {
                        session.EnableProvider(name, TraceEventLevel.Verbose);
                        Console.WriteLine($"enabled {name}");
                    }
                }

                session.Source.Process();
            }
        }
    }
}
