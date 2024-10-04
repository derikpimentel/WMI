import wmi # pip install wmi
c = wmi.WMI()
black_list = ['str', 'bool', 'int', 'NoneType', 'tuple', 'dict']

def stop(element=None):
    command = input().lower() # PAUSA
    
    # Comando para finalizar
    if command == "exit":
        exit()

    # Comando para saída do laço
    elif command == "skip":
        return True
    
    elif element:

        # Comando para especificação de propriedades
        if command == "specs":
            # Lista as propriedades do objeto
            properties = list(element.__dict__['_properties'])

            for item in properties:
                value = getattr(element, item)
                if not (type(value).__name__ in black_list):
                    print(f"specs {item}")
                    print(value)

                    if stop(value):
                        break

def show(element):
    for item in element:
        print(item)

        if stop(item):
            break

# A classe WMI Win32_1394Controller representa os recursos e o gerenciamento de um controlador 1394. O IEEE 1394 é uma especificação para um barramento serial de alta velocidade.
show(c.Win32_1394Controller())

# A classe WMI de associação Win32_1394ControllerDevice relaciona o controlador de barramento serial de alta velocidade (IEEE 1394 Firewire) e a instância CIM_LogicalDevice conectada a ele. Esse barramento serial fornece conectividade aprimorada para uma ampla variedade de dispositivos, incluindo componentes de áudio ou vídeo do consumidor, periféricos de armazenamento, outros computadores e dispositivos portáteis. O IEEE 1394 foi adotado pelo setor de eletrônicos de consumo e fornece uma interface de expansão compatível com Plug and Play.
show(c.Win32_1394ControllerDevice())

# A classe WMI Win32_Fan representa as propriedades de um dispositivo ventilador no sistema do computador. Por exemplo, o ventilador de resfriamento da CPU.
show(c.Win32_Fan())

# A classe WMIWin32_HeatPipe representa as propriedades de um dispositivo de resfriamento de pipe de calor.
show(c.Win32_HeatPipe())

# A classe WMI Win32_Refrigeration representa as propriedades de um dispositivo de refrigeração.
show(c.Win32_Refrigeration())

# A classe WMI Win32_TemperatureProbe representa as propriedades de um sensor de temperatura (termômetro eletrônico).
show(c.Win32_TemperatureProbe())
## OBS.: A maioria das informações fornecidas pela classe WMI Win32_TemperatureProbe vem do SMBIOS. Leituras em tempo real para a propriedade CurrentReading não podem ser extraídas de tabelas SMBIOS. Por esse motivo, as implementações atuais do WMI não preenchem a propriedade CurrentReading . A presença da propriedade CurrentReading é reservada para uso futuro.

# A classe WMI de associação Win32_AssociatedProcessorMemory relaciona um processador e sua memória de cache.
show(c.Win32_AssociatedProcessorMemory())

# A classe WMI Win32_AutochkSetting representa as configurações para a operação de verificação automática de um disco.
show(c.Win32_AutochkSetting())

# A classe WMI Win32_BaseBoard representa um quadro base, que também é conhecido como placa-mãe ou placa-mãe do sistema.
show(c.Win32_BaseBoard())

# A classe WMI Win32_Battery representa uma bateria conectada ao sistema do computador.
show(c.Win32_Battery())

# A classe WMI Win32_BIOS representa os atributos dos BIOS (serviços básicos de entrada/saída) do sistema de computador instalados em um computador.
show(c.Win32_BIOS())

# A classe WMI Win32_Bus representa um barramento físico, conforme visto por um computador que executa um sistema operacional Windows. Qualquer instância de um barramento do Windows é um descendente (ou membro) dessa classe.
show(c.Win32_Bus())

# A classe WMI Win32_CacheMemory representa memória de cache interna e externa em um sistema de computador.
show(c.Win32_CacheMemory())

# A classe WMI Win32_CDROMDrive representa uma unidade CD-ROM em um sistema de computador que executa o Windows.
show(c.Win32_CDROMDrive())
## OBS.: Lembre-se de que o nome da unidade não corresponde à letra da unidade lógica atribuída ao dispositivo.

# A classe WMI de associação Win32_CIMLogicalDeviceCIMDataFile relaciona dispositivos lógicos e arquivos de dados, indicando os arquivos de driver usados pelo dispositivo. Essa classe é usada para descobrir quais drivers de dispositivo um dispositivo usa.
show(c.Win32_CIMLogicalDeviceCIMDataFile())

# A classe WMI de associação Win32_ComputerSystemProcessor relaciona um sistema de computador e um processador em execução nesse sistema.
show(c.Win32_ComputerSystemProcessor())

# A classe WMI Win32_CurrentProbe representa as propriedades de um sensor de monitoramento atual (ammeter).
show(c.Win32_CurrentProbe())

# A classe WMI Win32_DesktopMonitor representa o tipo de monitor ou dispositivo de exibição anexado ao sistema do computador.
show(c.Win32_DesktopMonitor())
## OBS.: O hardware que não é compatível com o WDDM (Modelo de Driver de Exibição do Windows) retorna valores de propriedade imprecisos para instâncias dessa classe.

# A classe WMI de associação Win32_DeviceBus relaciona um barramento do sistema e um dispositivo lógico usando o barramento. Essa classe é usada para descobrir quais dispositivos estão em qual barramento.
show(c.Win32_DeviceBus())

# O Win32_DeviceChangeEventclasse WMI abstrata representa eventos de alteração de dispositivo resultantes da adição, remoção ou modificação de dispositivos no sistema de computador. Isso inclui alterações na configuração de hardware (encaixe e desencaixagem), no estado de hardware ou em dispositivos mapeados recentemente (mapeamento de uma unidade de rede). Por exemplo, um dispositivo foi alterado quando uma mensagem de WM_DEVICECHANGE é enviada.
show(c.Win32_DeviceChangeEvent())

# A classe WMI Win32_DeviceMemoryAddress representa um endereço de memória do dispositivo em um sistema de computador que executa o Windows.
show(c.Win32_DeviceMemoryAddress())

# O Win32_DeviceSettingsclasse WMI abstrata e de associação relaciona um dispositivo lógico e uma configuração que pode ser aplicada a ele.
show(c.Win32_DeviceSettings())

# A classe WMI do Win32_DiskDrive representa uma unidade de disco física como visto por um computador que executa o sistema operacional Windows.
show(c.Win32_DiskDrive())

# A classe WMI de associação Win32_DiskDriveToDiskPartition relaciona uma unidade de disco e uma partição existente nela.
show(c.Win32_DiskDriveToDiskPartition())

# A classe WMI Win32_DiskPartition representa os recursos e a capacidade de gerenciamento de uma área particionada de um disco físico em um sistema de computador que executa o Windows. Exemplo: Disco nº 0, Partição nº 1.
show(c.Win32_DiskPartition())

# A classe WMIWin32_DisplayControllerConfiguration representa as informações de configuração do adaptador de vídeo de um sistema de computador que executa o Windows.
show(c.Win32_DisplayControllerConfiguration())
# OBS.: Essa classe está obsoleta. No lugar dessa classe, você deve usar as propriedades nas classes Win32_VideoController, Win32_DesktopMonitor e CIM_VideoControllerResolution.

# A classe WMI Win32_DMAChannel representa um canal de DMA (acesso direto à memória) em um sistema de computador que executa o Windows. O DMA é um método de mover dados de um dispositivo para a memória (ou vice-versa) sem a ajuda do microprocessador. A placa do sistema usa um controlador DMA para lidar com um número fixo de canais, cada um dos quais pode ser usado por um (e apenas um) dispositivo por vez.
show(c.Win32_DMAChannel())

# A classe WMI de associação Win32_DriverForDevice relaciona uma instância de impressora a uma instância de driver de impressora.
show(c.Win32_DriverForDevice())

# A classe WMI Win32_FloppyController representa os recursos e a capacidade de gerenciamento de um controlador de unidade de disco disquete.
#show(c.Win32_FloppyController())
""" OBS.: Win32_FloppyController não está mais disponível para uso a partir de Windows 10 e Windows Server 2016. """

# A classe WMI Win32_FloppyDrive gerencia as funções de uma unidade de disco disquete.
#show(c.Win32_FloppyDrive())
""" OBS.: Win32_FloppyDrive não está mais disponível para uso a partir de Windows 10 e Windows Server 2016. """

# A classe WMI Win32_IDEController gerencia os recursos de um dispositivo de controlador IDE (dispositivo eletrônico integrado).
show(c.Win32_IDEController())

# A classe WMI de associação Win32_IDEControllerDevice relaciona um controlador IDE (Integrated Drive Electronics) e o dispositivo lógico conectado a, por exemplo, uma unidade de disco.
show(c.Win32_IDEControllerDevice())

# A classe WMI Win32_InfraredDevice representa os recursos e o gerenciamento de um dispositivo infravermelho.
show(c.Win32_InfraredDevice())

# A classe WMI Win32_IRQResource representa um número IRQ (linha de solicitação de interrupção) em um sistema de computador que executa o Windows. Uma solicitação de interrupção é um sinal enviado à CPU por um dispositivo ou programa para eventos críticos de tempo. O IRQ pode ser baseado em hardware ou em software.
show(c.Win32_IRQResource())

# A classe WMI Win32_Keyboard representa um teclado instalado em um sistema de computador que executa o Windows.
show(c.Win32_Keyboard())

# A classe WMI Win32_LogicalDisk representa uma fonte de dados que é resolvida para um dispositivo de armazenamento local real em um sistema de computador que executa o Windows.
show(c.Win32_LogicalDisk())

# A classe WMI de associação Win32_LogicalDiskRootDirectory relaciona um disco lógico e sua estrutura de diretório.
show(c.Win32_LogicalDiskRootDirectory())

# A classe WMI de associação Win32_LogicalDiskToPartition relaciona uma unidade de disco lógica e a partição de disco em que ela reside.
show(c.Win32_LogicalDiskToPartition())

# A classe WMI Win32_LogicalProgramGroup representa um grupo de programas em um sistema de computador que executa o Windows. Por exemplo, Acessórios ou Inicialização.
show(c.Win32_LogicalProgramGroup())

# A classe WMI de associação Win32_LogicalProgramGroupDirectory relaciona grupos de programas lógicos (agrupamentos no menu Iniciar) e os diretórios de arquivo nos quais eles são armazenados.
show(c.Win32_LogicalProgramGroupDirectory())

# A classe WMI Win32_LogicalProgramGroupItem representa um elemento contido por um Win32_LogicalProgramGroup que também não é outra instância Win32_LogicalProgramGroup.
show(c.Win32_LogicalProgramGroupItem())

# A classe WMI de associação Win32_LogicalProgramGroupItemDataFile relaciona os itens do grupo de programas do menu Iniciar e os arquivos nos quais eles são armazenados.
show(c.Win32_LogicalProgramGroupItemDataFile())

# A classe WMI Win32_MappedLogicalDisk representa dispositivos de armazenamento de rede mapeados como discos lógicos no sistema de computador.
show(c.Win32_MappedLogicalDisk())

# A classe WMI Win32_MemoryArray representa as propriedades da matriz de memória do sistema do computador e dos endereços mapeados.
show(c.Win32_MemoryArray())

# A classe WMI de associação Win32_MemoryArrayLocation relaciona uma matriz de memória lógica e a matriz de memória física na qual ela existe.
show(c.Win32_MemoryArrayLocation())

# A classe WMI Win32_MemoryDevice representa as propriedades de um dispositivo de memória do sistema de computador e seus endereços mapeados associados.
show(c.Win32_MemoryDevice())

# A classe WMI de associação Win32_MemoryDeviceArray relaciona um dispositivo de memória e a matriz de memória na qual ele reside.
show(c.Win32_MemoryDeviceArray())

# A classe WMI de associação Win32_MemoryDeviceLocation relaciona um dispositivo de memória e a memória física em que ele existe.
show(c.Win32_MemoryDeviceLocation())

# A classe WMI Win32_MotherboardDevice representa um dispositivo que contém os componentes centrais do sistema de computador Windows.
show(c.Win32_MotherboardDevice())

# A classe Win32_NetworkAdapter foi preterida. Em vez disso, use a classe MSFT_NetAdapter . A classe WMIWin32_NetworkAdapter representa um adaptador de rede de um computador que executa um sistema operacional Windows.
show(c.Win32_NetworkAdapter())
## OBS.: Win32_NetworkAdapter fornece apenas dados IPv4. Para obter mais informações, consulte Suporte a IPv6 e IPv4 no WMI.

# A classe WMI Win32_NetworkAdapterConfiguration representa os atributos e comportamentos de um adaptador de rede. Essa classe inclui propriedades e métodos extras que dão suporte ao gerenciamento do protocolo TCP/IP que são independentes do adaptador de rede.
show(c.Win32_NetworkAdapterConfiguration())

# A classe WMI de associação Win32_NetworkAdapterSetting relaciona um adaptador de rede e suas definições de configuração.
show(c.Win32_NetworkAdapterSetting())

# A classe WMI Win32_NetworkClient representa um cliente de rede em um sistema Windows. Qualquer sistema de computador na rede com uma relação de cliente com o sistema é um descendente (ou membro) dessa classe.
show(c.Win32_NetworkClient())

# A classe WMI Win32_NetworkConnection representa uma conexão de rede ativa em um ambiente baseado no Windows.
show(c.Win32_NetworkConnection())

# A classe WMI Win32_NetworkLoginProfile representa as informações de logon de rede de um usuário específico em um sistema de computador que executa o Windows. Isso inclui, mas não se limita a status de senha, privilégios de acesso, cotas de disco e caminhos de diretório de logon.
show(c.Win32_NetworkLoginProfile())

# A classe WMI Win32_NetworkProtocol representa um protocolo e suas características de rede em um sistema de computador Win32.
show(c.Win32_NetworkProtocol())

# A classe WMI Win32_OnBoardDevice representa dispositivos de adaptador comuns integrados à placa-mãe (placa-mãe).
show(c.Win32_OnBoardDevice())

# A classe WMI Win32_ParallelPort representa as propriedades de uma porta paralela em um sistema de computador que executa o Windows.
show(c.Win32_ParallelPort())

# A classe WMI Win32_PCMCIAController gerencia os recursos de um dispositivo controlador PCMCIA (Adaptador de Interface de Cartão de Memória de Computador Pessoal) de um pc card.
show(c.Win32_PCMCIAController())

# A classe WMI Win32_PhysicalMemory representa um dispositivo de memória física localizado em um sistema de computador e disponível para o sistema operacional.
show(c.Win32_PhysicalMemory())

# A classe WMI Win32_PhysicalMemoryArray representa detalhes sobre a memória física do sistema do computador. Isso inclui o número de dispositivos de memória, a capacidade de memória disponível e o tipo de memória, por exemplo, memória de sistema ou vídeo.
show(c.Win32_PhysicalMemoryArray())

# A classe WMI de associação Win32_PhysicalMemoryLocation relaciona uma matriz de memória física e sua memória física.
show(c.Win32_PhysicalMemoryLocation())

# A classe WMI de associação Win32_PnPAllocatedResource representa uma associação entre dispositivos lógicos e recursos do sistema. Essa classe é usada para descobrir os recursos que estão em uso por um dispositivo específico, como um IRQ (Interrupt ReQuest) ou um canal de Acesso direto à memória (DMA).
show(c.Win32_PnPAllocatedResource())

# A associação Win32_PnPDevice na classe WMI relaciona um dispositivo (conhecido pelo Gerenciador de Configurações como uma PNPEntity) e a função que ele executa. Sua função é representada por uma subclasse do dispositivo lógico que descreve seu uso. Por exemplo, uma instância de Win32_Keyboard ou Win32_DiskDrive. Ambos os objetos referenciados representam o mesmo dispositivo do sistema subjacente. As alterações na alocação de recursos no lado do PNPEntity afetarão o dispositivo associado.
show(c.Win32_PnPDevice())

# O tipo base para classes que representam uma propriedade retornada pelo método Win32_PnPEntity::GetDeviceProperties.
show(c.Win32_PnPDeviceProperty())

# Representa uma propriedade de dispositivo PnP do tipo Uint8.
show(c.Win32_PnPDevicePropertyUint8())

# Representa uma propriedade de dispositivo PnP do tipo Uint16.
show(c.Win32_PnPDevicePropertyUint16())

# Representa uma propriedade de dispositivo PnP do tipo Uint32.
show(c.Win32_PnPDevicePropertyUint32())

# Representa uma propriedade de dispositivo PnP do tipo Uint64.
show(c.Win32_PnPDevicePropertyUint64())

# Representa uma propriedade de dispositivo PnP do tipo Sint8.
show(c.Win32_PnPDevicePropertySint8())

# Representa uma propriedade de dispositivo PnP do tipo Sint16.
show(c.Win32_PnPDevicePropertySint16())

# Representa uma propriedade de dispositivo PnP do tipo Sint32.
show(c.Win32_PnPDevicePropertySint32())

# Representa uma propriedade de dispositivo PnP do tipo Sint64.
show(c.Win32_PnPDevicePropertySint64())

# Representa uma propriedade de dispositivo PnP da cadeia de caracteres de tipo.
show(c.Win32_PnPDevicePropertyString())

# Representa uma propriedade de dispositivo PnP do tipo booliano.
show(c.Win32_PnPDevicePropertyBoolean())

# Representa uma propriedade de dispositivo PnP do tipo real32.
show(c.Win32_PnPDevicePropertyReal32())

# Representa uma propriedade de dispositivo PnP do tipo real64.
show(c.Win32_PnPDevicePropertyReal64())

# Representa uma propriedade de dispositivo PnP do tipo datetime.
show(c.Win32_PnPDevicePropertyDateTime())

# Representa uma propriedade de dispositivo PnP do tipo Win32_SecurityDescriptor.
show(c.Win32_PnPDevicePropertySecurityDescriptor())

# Representa uma propriedade de dispositivo PnP binário na forma de uma matriz Uint8.
show(c.Win32_PnPDevicePropertyBinary())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos Uint16.
show(c.Win32_PnPDevicePropertyUint16Array())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos Uint32.
show(c.Win32_PnPDevicePropertyUint32Array())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos Uint64.
show(c.Win32_PnPDevicePropertyUint64Array())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos Sint8.
show(c.Win32_PnPDevicePropertySint8Array())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos Sint16.
show(c.Win32_PnPDevicePropertySint16Array())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos Sint32.
show(c.Win32_PnPDevicePropertySint32Array())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos Sint64.
show(c.Win32_PnPDevicePropertySint64Array())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos de cadeia de caracteres.
show(c.Win32_PnPDevicePropertyStringArray())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos boolianos.
show(c.Win32_PnPDevicePropertyBooleanArray())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos real32.
show(c.Win32_PnPDevicePropertyReal32Array())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos real64.
show(c.Win32_PnPDevicePropertyReal64Array())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos datetime.
show(c.Win32_PnPDevicePropertyDateTimeArray())

# Representa uma propriedade de dispositivo PnP que consiste em uma matriz de elementos Win32_SecurityDescriptor.
show(c.Win32_PnPDevicePropertySecurityDescriptorArray())

# A classe WMI Win32_PnPEntity representa as propriedades de um dispositivo Plug and Play. Plug and Play entidades são mostradas como entradas no Gerenciador de Dispositivos localizado em Painel de Controle.
show(c.Win32_PnPEntity())

# A classe WMI Win32_PointingDevice representa um dispositivo de entrada usado para apontar e selecionar regiões na exibição de um sistema de computador que executa o Windows. Qualquer dispositivo usado para manipular um ponteiro ou apontar para a exibição em um sistema de computador que executa o Windows é um membro dessa classe.
show(c.Win32_PointingDevice())

# A classe WMI Win32_PortableBattery contém as propriedades relacionadas a uma bateria portátil, como uma bateria de computador notebook.
show(c.Win32_PortableBattery())

# A classe WMI Win32_PortConnector representa portas de conexão físicas, como pino DB-25 masculino, Centronics ou PS/2.
show(c.Win32_PortConnector())

# A classe WMI Win32_PortResource representa uma porta de E/S em um sistema de computador que executa o Windows.
show(c.Win32_PortResource())

# A classe WMI Win32_POTSModem representa os serviços e características de um modem pots (serviço telefônico antigo simples) em um sistema de computador que executa o Windows.
show(c.Win32_POTSModem())

# A classe WMI de associação Win32_POTSModemToSerialPort relaciona um modem à porta serial que o modem usa.
show(c.Win32_POTSModemToSerialPort())

# A classe WMI Win32_Printer representa um dispositivo conectado a um computador em execução em um sistema operacional Microsoft Windows que pode produzir uma imagem impressa ou texto em papel ou em outro meio.
show(c.Win32_Printer())

# A classe WMI Win32_PrinterConfiguration representa a configuração de um dispositivo de impressora. Isso inclui recursos como resolução, cor, fontes e orientação.
show(c.Win32_PrinterConfiguration())

# A classe WMI de associação Win32_PrinterController relaciona uma impressora e o dispositivo local ao qual a impressora está conectada. Observe que essa classe retorna apenas instâncias para impressoras locais.
show(c.Win32_PrinterController())

# A classe WMI Win32_PrinterDriver representa os drivers de uma instância de Win32_Printer.
show(c.Win32_PrinterDriver())

# A classe WMI de associação Win32_PrinterDriverDll relaciona uma impressora local e seu arquivo de driver.
show(c.Win32_PrinterDriverDll())

# A classe WMI de associação Win32_PrinterSetting relaciona uma impressora e suas configurações.
show(c.Win32_PrinterSetting())

# A classe WMI de associação Win32_PrinterShare relaciona uma impressora local e o compartilhamento que a representa conforme ela é exibida em uma rede.
show(c.Win32_PrinterShare())

# A classe WMI Win32_PrintJob representa um trabalho de impressão gerado por um aplicativo do Windows. Qualquer unidade de trabalho gerada pelo comando de impressão de um aplicativo em execução em um computador em execução em um sistema operacional Windows é descendente ou membro dessa classe.
show(c.Win32_PrintJob())

# A classe WMI Win32_Processor representa um dispositivo que pode interpretar uma sequência de instruções em um computador em execução em um sistema operacional Windows.
show(c.Win32_Processor())

# A classe WMI Win32_SCSIController representa um controlador SCSI em um sistema de computador que executa o Windows.
show(c.Win32_SCSIController())

# A classe WMI de associação Win32_SCSIControllerDevice relaciona um controlador SCSI (interface do sistema de computador) pequeno e o dispositivo lógico (unidade de disco) conectado a ele.
show(c.Win32_SCSIControllerDevice())

# A classe WMI Win32_SerialPort representa uma porta serial em um sistema de computador que executa o Windows.
show(c.Win32_SerialPort())

# A classe WMI Win32_SerialPortConfiguration representa as configurações de transmissão de dados em uma porta serial baseada no Windows. Isso inclui configurações para estabelecer uma conexão e verificação de erros.
show(c.Win32_SerialPortConfiguration())

# A classe WMI de associação Win32_SerialPortSetting relaciona uma porta serial e suas configurações.
show(c.Win32_SerialPortSetting())

# O Win32_SMBIOSMemoryclasse WMI abstrata representa as propriedades de uma memória do sistema de computador, conforme visto por meio da interface SMBIOS (BIOS de gerenciamento do sistema). A interface SMBIOS não distingue entre memórias não voláteis, voláteis e flash. A classe CIM_Memory é a classe pai de todos os tipos de memória.
show(c.Win32_SMBIOSMemory())

# A classe WMI Win32_SoundDevice representa as propriedades de um dispositivo de som em um sistema de computador que executa o Windows.
show(c.Win32_SoundDevice())

# A classe WMI Win32_TapeDrive representa uma unidade de fita em um sistema de computador que executa o Windows. As unidades de fita são distinguidas principalmente pelo fato de que elas só podem ser acessadas sequencialmente.
show(c.Win32_TapeDrive())

# A classe WMI Win32_TCPIPPrinterPort representa um ponto de acesso de serviço TCP/IP.
show(c.Win32_TCPIPPrinterPort())

# A classe WMI Win32_USBController gerencia os recursos de um controlador de barramento serial universal (USB).
show(c.Win32_USBController())

# A classe WMI de associação de Win32_USBControllerDevice relaciona um controlador USB (barramento serial universal) e a instância CIM_LogicalDevice conectada a ele.
show(c.Win32_USBControllerDevice())

# A classe WMI Win32_VideoController representa os recursos e a capacidade de gerenciamento do controlador de vídeo em um sistema de computador que executa o Windows.
show(c.Win32_VideoController())
## OBS.: O hardware que não é compatível com o WDDM (Modelo de Driver de Exibição do Windows) retorna valores de propriedade imprecisos para instâncias dessa classe.

# A classe WMI de associação Win32_VideoSettings relaciona um controlador de vídeo e configurações de vídeo que podem ser aplicadas a ela.
show(c.Win32_VideoSettings())

# A classe WMI Win32_VoltageProbe representa as propriedades de um sensor de tensão (voltômetro eletrônico).
show(c.Win32_VoltageProbe())