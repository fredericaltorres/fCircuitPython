using System;
using System.Collections.Generic;
using System.JSON;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ArduinoWindowsConsole
{
    //public enum ComCommandType // Do not change the order of the enum type for compatibilty reason
    //{
    //    Help,
    //    Quit,
    //    Send,
    //    PauseProcessingFromDevice,
    //    CtrlC,
    //    CtrlD,
    //    Unknown,
    //}
    public class ComCommand
    {
        public string Caption;
        public string Command;
        public ConsoleKey ConsoleKey;
    }
    /// <summary>
    /// Describe the possible communication between the app running on the Arduino and the 
    /// this Windows Console
    /// </summary>
    public class ComConfig : JSonPersistedObject
    {
        public string PortName;
        public int BaudRate;
        public string DeviceName;

        public static ComConfig Load(string fileName)
        {
            ComConfig o = JSonPersistedObject.Load<ComConfig>(fileName);
            o.FileName = fileName;
            if (o.BaudRate == 0)
                o.BaudRate = 9600;
            return o;
        }
    }
}
