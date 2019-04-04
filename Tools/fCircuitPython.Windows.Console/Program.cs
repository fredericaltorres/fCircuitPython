using System;
using System.Data;
using System.IO;
using System.IO.Ports;
using System.Reflection;
using ArduinoLibrary;
using ArduinoWindowsConsole;
using DynamicSugar;
using System.Runtime.InteropServices;
using System.Collections.Generic;

namespace test
{
    class Program
    {
        private static ComConfig _comConfig;

        static void WriteLine(string text, ConsoleColor c)
        {
            var color = Console.ForegroundColor;
            Console.ForegroundColor = c;
            Console.WriteLine(text);
            Console.ForegroundColor = color;
        }

        static void Write(string text, ConsoleColor c)
        {
            var color = Console.ForegroundColor;
            Console.ForegroundColor = c;
            Console.Write(text);
            Console.ForegroundColor = color;
        }

        static void SendCommandCtrlC(SerialPortManager ac)
        {
            WriteLine("Ctrl+C", ConsoleColor.Cyan);
            ac.SendBuffer(new List<byte>() { 3 });
        }
        static void SendCommandCtrlD(SerialPortManager ac)
        {
            WriteLine("Ctrl+D", ConsoleColor.Cyan);
            ac.SendBuffer(new List<byte>() { 4 });
        }
        static void SendCommandChar(SerialPortManager ac, char c)
        {
            Write(c.ToString(), ConsoleColor.Cyan);
            ac.SendBuffer(new List<byte>() { (byte)c });
        }

        static void SendCommand(SerialPortManager ac, string command)
        {
            WriteLine(command, ConsoleColor.Cyan);
            ac.Send(command);
        }

        private static void PrintHelp()
        {
            var m = $"{_comConfig.DeviceName} - port:{_comConfig.PortName}";
            Console.Title = m;

            m += " - F1:Help, F3:Quit, F2:REPL, Ctrl-D:Resume execution";
            WriteLine(m, ConsoleColor.Cyan);
        }

        static string GetConfigFileName()
        {
            return Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "ArduinoWindowsConsole.json");
        }

        static void InitConfig()
        {
            _comConfig = ComConfig.Load(GetConfigFileName());
        }

        static void Main(string[] args)
        {
            var goOn = true;
            var processQueue = true;

            InitConfig();
            PrintHelp();

            bool displayPaused = false;

            using (var ac = new SerialPortManager(_comConfig.PortName, _comConfig.BaudRate))
            {
                while (goOn)
                {
                    if (Console.KeyAvailable)
                    {
                        var k = Console.ReadKey(true);
                        switch (k.Key)
                        {                            
                            case ConsoleKey.F1:  Console.Clear(); PrintHelp(); break;
                            case ConsoleKey.F2:
                                SendCommandCtrlC(ac);
                                SendCommandChar(ac, ' ');
                                SendCommandChar(ac, '\r');
                                break;
                            case ConsoleKey.D:
                                if (k.Modifiers == ConsoleModifiers.Control)
                                    SendCommandCtrlD(ac);
                                else
                                    SendCommandChar(ac, k.KeyChar);
                                break;
                            case ConsoleKey.F3: goOn = false; break;
                            default:
                                SendCommandChar(ac, k.KeyChar);
                                break;
                        }
                    }
                    if (processQueue && ac.ReceivedMessages.Count > 0)
                    {
                        var message = ac.ReceivedMessages.Dequeue();
                        Console.WriteLine(message);
                        var processRow = true;
                        if ((!displayPaused) && (processRow))
                        {
                            
                        }
                    }
                }
            }
        }
    }
}