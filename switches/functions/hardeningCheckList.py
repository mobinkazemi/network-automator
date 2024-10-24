
hardeningCheckList = [
    {
        "title": "1.1.1 Enable 'aaa new-model' (Scored) ",
        "description": "This command enables the AAA access control system.  ",
        "audit": "Perform the following to determine if AAA services are enabled:  hostname#show running-config | incl aaa new-model  8   If the result includes a \"no\", the feature is not enabled.  ",
        "command": "show running-config | incl aaa new-model",
        "recommendations": "Globally enable authentication, authorization and accounting (AAA) using the new-model command. hostname(config)#aaa new-model Impact: Implementing Cisco AAA is significantly disruptive as former access methods are immediately disabled. Therefore, before implementing Cisco AAA, the organization should carefully review and plan their authentication criteria (logins & passwords, challenges & responses, and token technologies), authorization methods, and accounting requirements. Default Value: AAA is not enabled.  "
    },
    {
        "title": "1.1.2 Enable 'aaa authentication login' (Scored) ",
        "description": "Sets authentication, authorization and accounting (AAA) authentication at login.  ",
        "audit": "Perform the following to determine if AAA authentication for login is enabled: hostname#show run | incl aaa authentication login If a result does not return, the feature is not enabled.  ",
        "command": "show run | incl aaa authentication login",
        "recommendations": "Configure AAA authentication method(s) for login authentication. hostname(config)#aaa authentication login {default | aaa_list_name} [passwd-expiry] method1 [method2] Impact: Implementing Cisco AAA is significantly disruptive as former access methods are immediately disabled. Therefore, before implementing Cisco AAA, the organization should carefully review and plan their authentication methods such as logins and passwords, challenges and responses, and which token technologies will be used. Default Value: AAA authentication at login is disabled.  "
    },
    {
        "title": "1.1.3 Enable 'aaa authentication enable default' (Scored) ",
        "description": "Authenticates users who access privileged EXEC mode when they use the enable command.  ",
        "audit": "Perform the following to determine if AAA authentication enable mode is enabled: hostname#show running-config | incl aaa authentication enable If a result does not return, the feature is not enabled  ",
        "command": "show running-config | incl aaa authentication enable ",
        "recommendations": "Configure AAA authentication method(s) for enable authentication. hostname(config)#aaa authentication enable default method1 enable  Impact: Enabling Cisco AAA 'authentication enable' mode is significantly disruptive as former access methods are immediately disabled. Therefore, before enabling  'aaa authentication enable default' mode, the organization should plan and implement authentication logins and passwords, challenges and responses, and token technologies. Default Value: By default, fallback to the local database is disabled.  "
    },
    {
        "title": "1.1.4 Set 'login authentication for 'line con 0' (Scored) ",
        "description": "Authenticates users who access the router or switch using the serial console port. http://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-a1.html#GUID-4171D649-2973-4707-95F3-9D96971893D0http://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-a1.html#GUID-4171D649-2973-4707-95F3-9D96971893D011    ",
        "audit": "Perform the following to determine if AAA authentication for line login is enabled: If the command does not return a result for each management access method, the feature is not enabled hostname#sh run | sec line | incl login authentication  ",
        "command": "sh run | sec line | incl login authentication ",
        "recommendations": "Configure management lines to require login using the default or a named AAA authentication list. This configuration must be set individually for all line types. hostname(config)#line console 0 hostname(config-line)#login authentication {default | aaa_list_name} Impact: Enabling Cisco AAA 'line login' is significantly disruptive as former access methods are immediately disabled. Therefore, before enabling Cisco AAA 'line login',  the organization should plan and implement authentication logins and passwords, challenges and responses, and token technologies. Default Value: Login authentication is not enabled. Uses the default set with aaa authentication login.  "
    },
    {
        "title": "1.1.5 Set 'login authentication for 'line tty' (Scored) ",
        "description": "Authenticates users who access the router or switch using the TTY port.  ",
        "audit": "Perform the following to determine if AAA authentication for line login is enabled: If the command does not return a result for each management access method, the feature is not enabled hostname#sh run | sec line | incl login authentication  ",
        "command": "sh run | sec line | incl login authentication ",
        "recommendations": "Configure management lines to require login using the default or a named AAA authentication list. This configuration must be set individually for all line types. hostname(config)#line tty {line-number} [ending-line-number] hostname(config-line)#login authentication {default | aaa_list_name} Impact: Enabling Cisco AAA 'login authentication for line TTY' is significantly disruptive as former access methods are immediately disabled. Therefore, before enabling Cisco AAA 'login authentication for line TTY',  the organization should plan and implement authentication logins and passwords, challenges and responses, and token technologies. Default Value: Login authentication is not enabled. Uses the default set with aaa authentication login.  "
    },
    {
        "title": "1.1.6 Set 'login authentication for 'line vty' (Scored) ",
        "description": "Authenticates users who access the router or switch remotely through the VTY port.  ",
        "audit": "Perform the following to determine if AAA authentication for line login is enabled: If the command does not return a result for each management access method, the feature is not enabled hostname#sh run | sec line | incl login authentication  ",
        "command": "sh run | sec line | incl login authentication ",
        "recommendations": "Configure management lines to require login using the default or a named AAA authentication list. This configuration must be set individually for all line types. hostname(config)#line vty {line-number} [ending-line-number] hostname(config-line)#login authentication {default | aaa_list_name} Impact: Enabling Cisco AAA 'login authentication for line VTY' is significantly disruptive as former access methods are immediately disabled. Therefore, before enabling Cisco AAA 'login authentication for line VTY', the organization should plan and implement authentication logins and passwords, challenges and responses, and token technologies. Default Value: http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-k1.html#GUID-297BDF33-4841-441C-83F3-4DA51C3C7284http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-k1.html#GUID-297BDF33-4841-441C-83F3-4DA51C3C728414   Login authentication is not enabled. Uses the default set with aaa authentication login.  "
    },
    {
        "title": "1.1.8 Set 'aaa accounting connection' (Scored) ",
        "description": "Provides information about all outbound connections made from the network access server.  ",
        "audit": "Perform the following to determine if aaa accounting for connection is required: Verify a command string result returns hostname#sh run | incl aaa accounting connection  ",
        "command": "sh run | incl aaa accounting connection",
        "recommendations": "16   Configure AAA accounting for connections. hostname(config)#aaa accounting connection {default | list-name | guarantee-first}  {start-stop | stop-only | none} {radius | group group-name} Impact: Implementing aaa accounting connection creates accounting records about connections from the network access server. Organizations should regular monitor these connection records for exceptions, remediate issues, and report findings regularly. Default Value: AAA accounting is not enabled.  "
    },
    {
        "title": "1.1.9 Set 'aaa accounting exec' (Scored) ",
        "description": "Runs accounting for the EXEC shell session.  ",
        "audit": "Perform the following to determine if aaa accounting for EXEC shell session is required: http://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-a1.html#GUID-0520BCEF-89FB-4505-A5DF-D7F1389F1BBAhttp://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-a1.html#GUID-0520BCEF-89FB-4505-A5DF-D7F1389F1BBA17   Verify a command string result returns hostname#sh run | incl aaa accounting exec  ",
        "command": "sh run | incl aaa accounting exec",
        "recommendations": "Configure AAA accounting for EXEC shell session. hostname(config)#aaa accounting exec {default | list-name | guarantee-first}  {start-stop | stop-only | none} {radius | group group-name} Impact: Enabling aaa accounting exec creates accounting records for the EXEC terminal sessions on the network access server. These records include start and stop times, usernames, and date information. Organizations should regularly monitor these records for exceptions, remediate issues, and report findings. Default Value: AAA accounting is not enabled.  "
    },
    {
        "title": "1.1.10 Set 'aaa accounting network' (Scored) ",
        "description": "Runs accounting for all network-related service requests.  ",
        "audit": "Perform the following to determine if aaa accounting for connection is required: Verify a command string result returns hostname#sh run | incl aaa accounting network  ",
        "command": "sh run | incl aaa accounting network",
        "recommendations": "Configure AAA accounting for connections. hostname(config)#aaa accounting network {default | list-name | guarantee-first}  {start-stop | stop-only | none} {radius | group group-name} Impact: Implementing aaa accounting network creates accounting records for a method list including ARA, PPP, SLIP, and NCPs sessions. Organizations should regular monitor these records for exceptions, remediate issues, and report findings. Default Value: AAA accounting is not enabled.  "
    },
    # {
    #     "title": "1.1.11 Set 'aaa accounting system' (Scored) ",
    #     "description": "Performs accounting for all system-level events not associated with users, such as reloads.  ",
    #     "audit": "Perform the following to determine if aaa accounting system is required: Verify a command string result returns hostname#sh run | incl aaa accounting system  ",
    #     "command": "sh run | incl aaa accounting system",
    #     "recommendations": "Configure AAA accounting system. hostname(config)#aaa accounting system {default | list-name | guarantee-first}  {start-stop | stop-only | none} {radius | group group-name} Impact: Enabling aaa accounting system creates accounting records for all system-level events. Organizations should regular monitor these records for exceptions, remediate issues, and report findings regularly. Default Value: AAA accounting is not enabled.  "
    # },
    # {
    #     "title": "1.2.1 Set 'privilege 1' for local users (Scored) ",
    #     "description": "Sets the privilege level for the user.  ",
    #     "audit": "Perform the following to determine if a user with an encrypted password is enabled: Verify all username results return \"privilege 1\" hostname#show run | incl privilege  ",
    #     "command": "show run | incl privilege",
    #     "recommendations": "Set the local user to privilege level 1. hostname(config)#username <LOCAL_USERNAME> privilege 1  Impact: Organizations should create policies requiring all local accounts with 'privilege level 1' with encrypted passwords to reduce the risk of unauthorized access. Default configuration settings do not provide strong user authentication to the device. 21    "
    # },
    # {
    #     "title": "1.2.2 Set 'transport input ssh' for 'line vty' connections (Scored) ",
    #     "description": "Selects the Secure Shell (SSH) protocol.  ",
    #     "audit": "Perform the following to determine if SSH is the only transport method for incoming VTY logins: The result should show only \"ssh\" for \"transport input\" hostname#sh run | sec vty     ",
    #     "command": "sh run | sec vty",
    #     "recommendations": "Apply SSH to transport input on all VTY management lines hostname(config)#line vty <line-number> <ending-line-number> hostname(config-line)#transport input ssh  Impact: To reduce risk of unauthorized access, organizations should require all VTY management line protocols to be limited to ssh.  "
    # },
    # {
    #     "title": "1.2.3 Set 'no exec' for 'line aux 0' (Scored) ",
    #     "description": "The 'no exec' command restricts a line to outgoing connections only.  ",
    #     "audit": "Perform the following to determine if the EXEC process for the aux port is disabled: Verify no exec hostname#sh run | sec aux Verify you see the following \"no exec\" hostname#sh line aux 0 | incl exec  ",
    #     "command": "sh run | sec aux Verify ",
    #     "recommendations": "Disable the EXEC process on the auxiliary port. hostname(config)#line aux 0 hostname(config-line)#no exec Impact: Organizations can reduce the risk of unauthorized access by disabling the 'aux' port with the 'no exec' command. Conversely, not restricting access through the 'aux' port increases the risk of remote unauthorized access.  "
    # },
    # {
    #     "title": "1.2.4 Create 'access-list' for use with 'line vty' (Not Scored) ",
    #     "description": "Access lists control the transmission of packets on an interface, control Virtual Terminal Line (VTY) access, and restrict the contents of routing updates. The Cisco IOS software stops checking the extended access list after a match occurs.  ",
    #     "audit": "Perform the following to determine if the ACL is created: Verify the appropriate access-list definitions hostname#sh ip access-list <vty_acl_number>  ",
    #     "command": "sh ip access-list <vty_acl_number>",
    #     "recommendations": "Configure the VTY ACL that will be used to restrict management access to the device. hostname(config)#access-list <vty_acl_number> permit tcp <vty_acl_block_with_mask> any hostname(config)#access-list <vty_acl_number> permit tcp host <vty_acl_host> any hostname(config)#deny ip any any log Impact: http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-429A2B8C-FC26-49C4-94C4-0FD99C32EC34http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-429A2B8C-FC26-49C4-94C4-0FD99C32EC34http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-429A2B8C-FC26-49C4-94C4-0FD99C32EC3424   Organizations can reduce the risk of unauthorized access by implementing access-lists for all VTY lines. Conversely, using VTY lines without access-lists increases the risk of unauthorized access.  "
    # },
    # {
    #     "title": "1.2.5 Set 'access-class' for 'line vty' (Scored) ",
    #     "description": "The 'access-class' setting restricts incoming and outgoing connections between a particular vty (into a Cisco device) and the networking devices associated with addresses in an access list.  ",
    #     "audit": "Perform the following to determine if the ACL is set: Verify you see the access-class defined hostname#sh run | sec vty <line-number> <ending-line-number>  ",
    #     "command": "sh run | sec vty <line-number> <ending-line-number>",
    #     "recommendations": "Configure remote management access control restrictions for all VTY lines. hostname(config)#line vty <line-number> <ending-line-number> hostname(config-line)# access-class <vty_acl_number> in Impact: http://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-a2.html#GUID-9EA733A3-1788-4882-B8C3-AB0A2949120Chttp://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-a2.html#GUID-9EA733A3-1788-4882-B8C3-AB0A2949120C25   Applying 'access'class' to line VTY further restricts remote access to only those devices authorized to manage the device and reduces the risk of unauthorized access. Conversely, using VTY lines with 'access class' restrictions increases the risks of unauthorized access.  "
    # },
    # {
    #     "title": "1.2.6 Set 'exec-timeout' to less than or equal to 10 minutes for 'line aux ",
    #     "description": "If no input is detected during the interval, the EXEC facility resumes the current connection. If no connections exist, the EXEC facility returns the terminal to the idle state and disconnects the incoming session.  ",
    #     "audit": "Perform the following to determine if the timeout is configured: Verify you return a result NOTE: If you set an exec-timeout of 10 minutes, this will not show up in the configuration hostname#sh run | sec line aux 0  ",
    #     "command": "sh run | sec line aux 0",
    #     "recommendations": "Configure device timeout (10 minutes or less) to disconnect sessions after a fixed idle time. hostname(config)#line aux 0 hostname(config-line)#exec-timeout <timeout_in_minutes> <timeout_in_seconds> http://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-a2.html#GUID-FB9BC58A-F00A-442A-8028-1E9E260E54D3http://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-a2.html#GUID-FB9BC58A-F00A-442A-8028-1E9E260E54D326   Impact: Organizations should prevent unauthorized use of unattended or abandoned sessions by an automated control. Enabling 'exec-timeout' with an appropriate length of minutes or seconds prevents unauthorized access of abandoned sessions.  "
    # },
    # {
    #     "title": "1.2.7 Set 'exec-timeout' to less than or equal to 10 minutes 'line console ",
    #     "description": "If no input is detected during the interval, the EXEC facility resumes the current connection. If no connections exist, the EXEC facility returns the terminal to the idle state and disconnects the incoming session.  ",
    #     "audit": "Perform the following to determine if the timeout is configured: Verify you return a result NOTE: If you set an exec-timeout of 10 minutes, this will not show up in the configuration hostname#sh run | sec line con 0  ",
    #     "command": "sh run | sec line con 0",
    #     "recommendations": "http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE5419http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE5419http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE541927   Configure device timeout (10 minutes or less) to disconnect sessions after a fixed idle time. hostname(config)#line con 0 hostname(config-line)#exec-timeout <timeout_in_minutes> <timeout_in_seconds> Impact: Organizations should prevent unauthorized use of unattended or abandoned sessions by an automated control. Enabling 'exec-timeout' with an appropriate length reduces the risk of unauthorized access of abandoned sessions.  "
    # },
    # {
    #     "title": "1.2.8 Set 'exec-timeout' less than or equal to 10 minutes 'line tty' ",
    #     "description": "If no input is detected during the interval, the EXEC facility resumes the current connection. If no connections exist, the EXEC facility returns the terminal to the idle state and disconnects the incoming session.  ",
    #     "audit": "Perform the following to determine if the timeout is configured: Verify you return a result NOTE: If you set an exec-timeout of 10 minutes, this will not show up in the configuration http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE5419http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE5419http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE541928   hostname#sh line tty <tty_line_number> | begin Timeout  ",
    #     "command": "sh line tty <tty_line_number> | begin Timeout  ",
    #     "recommendations": "Configure device timeout (10 minutes or less) to disconnect sessions after a fixed idle time. hostname(config)#line tty {line_number} [ending_line_number] hostname(config-line)#exec-timeout <timeout_in_minutes> <timeout_in_seconds> Impact: Organizations should prevent unauthorized use of unattended or abandoned sessions by an automated control. Enabling 'exec-timeout' with an appropriate length reduces the risks of unauthorized access of abandoned sessions.  "
    # },
    # {
    #     "title": "1.2.9 Set 'exec-timeout' to less than or equal to 10 minutes 'line vty' ",
    #     "description": "If no input is detected during the interval, the EXEC facility resumes the current connection. If no connections exist, the EXEC facility returns the terminal to the idle state and disconnects the incoming session.  ",
    #     "audit": "Perform the following to determine if the timeout is configured: http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE5419http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE5419http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE541929   Verify you return a result NOTE: If you set an exec-timeout of 10 minutes, this will not show up in the configuration hostname#sh line vty <tty_line_number> | begin Timeout  ",
    #     "command": "sh line vty <tty_line_number> | begin Timeout ",
    #     "recommendations": "Configure device timeout (10 minutes or less) to disconnect sessions after a fixed idle time. hostname(config)#line vty {line_number} [ending_line_number] hostname(config-line)#exec-timeout <timeout_in_minutes> <timeout_in_seconds> Impact: Organizations should prevent unauthorized use of unattended or abandoned sessions by an automated control. Enabling 'exec-timeout' with an appropriate length of minutes or seconds prevents unauthorized access of abandoned sessions.  "
    # },
    # {
    #     "title": "1.2.10 Set 'transport input none' for 'line aux 0' (Scored)",
    #     "description": "When you want to allow only an outgoing connection on a line, use the no exec command.  ",
    #     "audit": "http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE5419http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE5419http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/D_through_E.html#GUID-76805E6F-9E89-4457-A9DC-5944C8FE541930   Perform the following to determine if inbound connections for the aux port are disabled: Verify you see the following \"Allowed input transports are none hostname#sh line aux 0 | incl input transports   ",
    #     "command": "sh line aux 0 | incl input transports ",
    #     "recommendations": "Disable the inbound connections on the auxiliary port. hostname(config)#line aux 0 hostname(config-line)#transport input none  Impact: Organizations should prevent all unauthorized access of auxiliary ports by disabling all protocols using the 'transport input none' command.   "
    # },
    # {
    #     "title": "1.3.1 Set the 'banner-text' for 'banner exec' (Scored) ",
    #     "description": "This command specifies a message to be displayed when an EXEC process is created (a line is activated, or an incoming connection is made to a vty). Follow this command with one or more blank spaces and a delimiting character of your choice. Then enter one or more lines of text, terminating the message with the second occurrence of the delimiting character. When a user connects to a router, the message-of-the-day (MOTD) banner appears first, followed by the login banner and prompts. After the user logs in to the router, the EXEC banner or incoming banner will be displayed, depending on the type of connection. For a reverse Telnet login, the incoming banner will be displayed. For all other connections, the router will display the EXEC banner. http://www.cisco.com/en/US/docs/ios/termserv/command/reference/tsv_s1.html#wp1069219http://www.cisco.com/en/US/docs/ios/termserv/command/reference/tsv_s1.html#wp106921931    ",
    #     "audit": "Perform the following to determine if the exec banner is set: hostname#sh running-config | beg banner exec  If the command does not return a result, the banner is not enabled  ",
    #     "command": "sh running-config | beg banner exec  If the command does not return a result, the banner is not enabled  ",
    #     "recommendations": "Configure the EXEC banner presented to a user when accessing the devices enable prompt. hostname(config)#banner exec c Enter TEXT message. End with the character 'c'. <banner-text> c Impact: Organizations provide appropriate legal notice(s) and warning(s) to persons accessing their networks by using a 'banner-text' for the banner exec command. Default Value: No banner is set by default  "
    # },
    # {
    #     "title": "1.3.2 Set the 'banner-text' for 'banner login' (Scored) ",
    #     "description": "Follow the banner login command with one or more blank spaces and a delimiting character of your choice. Then enter one or more lines of text, terminating the message with the second occurrence of the delimiting character. When a user connects to the router, the message-of-the-day (MOTD) banner (if configured) appears first, followed by the login banner and prompts. After the user successfully logs in to the router, the EXEC banner or incoming banner will be displayed, depending on the type of connection. For a reverse Telnet login, the incoming banner will be displayed. For all other connections, the router will display the EXEC banner.  ",
    #     "audit": "Perform the following to determine if the login banner is set: hostname#show running-config | beg banner login  http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/A_through_B.html#GUID-0DEF5B57-A7D9-4912-861F-E837C82A3881http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/A_through_B.html#GUID-0DEF5B57-A7D9-4912-861F-E837C82A3881http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/A_through_B.html#GUID-0DEF5B57-A7D9-4912-861F-E837C82A388133   If the command does not return a result, the banner is not enabled.  ",
    #     "command": "show running-config | beg banner login",
    #     "recommendations": "Configure the device so a login banner presented to a user attempting to access the device. hostname(config)#banner login c Enter TEXT message. End with the character 'c'. <banner-text> c Impact: Organizations provide appropriate legal notice(s) and warning(s) to persons accessing their networks by using a 'banner-text' for the banner login command. Default Value: No banner is set by default  "
    # },
    # {
    #     "title": "1.3.3 Set the 'banner-text' for 'banner motd' (Scored) ",
    #     "description": "This MOTD banner is displayed to all terminals connected and is useful for sending messages that affect all users (such as impending system shutdowns). Use the no exec-banner or no motd-banner command to disable the MOTD banner on a line. The no exec-banner command also disables the EXEC banner on the line.  When a user connects to the router, the MOTD banner appears before the login prompt. After the user logs in to the router, the EXEC banner or incoming banner will be displayed, depending on the type of connection. For a reverse Telnet login, the incoming banner will be displayed. For all other connections, the router will display the EXEC banner.   ",
    #     "audit": "Perform the following to determine if the login banner is set: hostname#sh running-config | beg banner motd  If the command does not return a result, the banner is not enabled.  ",
    #     "command": "sh running-config | beg banner motd"
    # },
    # {
    #     "title": "1.4.1 Set 'password' for 'enable secret' (Scored) ",
    #     "description": "Use the enable secret command to provide an additional layer of security over the enable password. The enable secret command provides better security by storing the enable secret password using a nonreversible cryptographic function. The added layer of security encryption provides is useful in environments where the password crosses the network or is stored on a TFTP server.  ",
    #     "audit": "Perform the following to determine enable secret is set: If the command does not return a result, the enable password is not set. hostname#sh run | incl enable secret   ",
    #     "command": "sh run | incl enable secret",
    #     "recommendations": "Configure a strong, enable secret password. hostname(config)#enable secret <ENABLE_SECRET_PASSWORD>  Impact: Organizations should protect privileged EXEC mode through policies requiring the 'enabling secret' setting, which enforces a one-way cryptographic hash (MD5). 36   Default Value: No enable secret password setup by default  "
    # },
    # {
    #     "title": "1.4.2 Enable 'service password-encryption' (Scored) ",
    #     "description": "When password encryption is enabled, the encrypted form of the passwords is displayed when a more system:running-config command is entered.  ",
    #     "audit": "Perform the following to determine if a user with an encrypted password is enabled: Ensure a result that matches the command return hostname#sh run | incl service password-encryption  ",
    #     "command": "sh run | incl service password-encryption",
    #     "recommendations": "Enable password encryption service to protect sensitive access passwords in the device configuration. hostname(config)#service password-encryption Impact: http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-e1.html#GUID-944C261C-7D4A-49E1-AA8F-C754750BDE47http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-e1.html#GUID-944C261C-7D4A-49E1-AA8F-C754750BDE4737   Organizations implementing 'service password-encryption' reduce the risk of unauthorized users learning clear text passwords to Cisco IOS configuration files. However, the algorithm used is not designed to withstand serious analysis and should be treated like clear-text. Default Value: Service password encryption is not set by default  "
    # },
    # {
    #     "title": "1.4.3 Set 'username secret' for all local users (Scored) ",
    #     "description": "Use the username secret command to configure a username and MD5-encrypted user password. MD5 encryption is a strong encryption method that is not retrievable; thus, you cannot use MD5 encryption with protocols that require clear-text passwords, such as Challenge Handshake Authentication Protocol (CHAP). The username secret command provides an additional layer of security over the username password. It also provides better security by encrypting the password using non reversible MD5 encryption and storing the encrypted text. The added layer of MD5 encryption is useful in environments in which the password crosses the network or is stored on a TFTP server.  ",
    #     "audit": "Perform the following to determine if a user with an encrypted password is enabled: http://www.cisco.com/en/US/docs/ios-xml/ios/security/s1/sec-cr-s1.html#GUID-CC0E305A-604E-4A74-8A1A-975556CE5871http://www.cisco.com/en/US/docs/ios-xml/ios/security/s1/sec-cr-s1.html#GUID-CC0E305A-604E-4A74-8A1A-975556CE587138   If a result does not return with secret, the feature is not enabled  hostname#show run | incl username  ",
    #     "command": "show run | incl username",
    #     "recommendations": "Create a local user with an encrypted, complex (not easily guessed) password. hostname(config)#username <LOCAL_USERNAME> secret <LOCAL_PASSWORD> Impact: Organizations implementing 'username secret' across their enterprise reduce the risk of unauthorized users gaining access to Cisco IOS devices by applying a MD5 hash and encrypting user passwords. Default Value: No passwords are set by default  "
    # },
    # {
    #     "title": "1.5.1 Set 'no snmp-server' to disable SNMP when unused (Scored) ",
    #     "description": "If not in use, disable simple network management protocol (SNMP), read and write access.  ",
    #     "audit": "Verify the result reads \"SNMP agent not enabled\" hostname#show snmp community  ",
    #     "command": "show snmp community",
    #     "recommendations": "Disable SNMP read and write access if not in used to monitor and/or manage device. hostname(config)#no snmp-server  Impact: Organizations not using SNMP should require all SNMP services to be disabled by running the 'no snmp-server' command.   "
    # },
    # {
    #     "title": "1.5.2 Unset 'private' for 'snmp-server community' (Scored) ",
    #     "description": "An SNMP community string permits read-only access to all objects.  ",
    #     "audit": "Perform the following to determine if the public community string is enabled: Ensure private does not show as a result hostname# show snmp community http://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-book.htmlhttp://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-book.html40    ",
    #     "command": " show snmp community ",
    #     "recommendations": "Disable the default SNMP community string \"private\" hostname(config)#no snmp-server community {private} Impact: To reduce the risk of unauthorized access, Organizations should disable default, easy to guess, settings such as the 'private' setting for snmp-server community.  "
    # },
    # {
    #     "title": "1.5.3 Unset 'public' for 'snmp-server community' (Scored) ",
    #     "description": "An SNMP community string permits read-only access to all objects.  ",
    #     "audit": "Perform the following to determine if the public community string is enabled: Ensure public does not show as a result hostname# show snmp community  ",
    #     "command": " show snmp community",
    #     "recommendations": "Disable the default SNMP community string \"public\" hostname(config)#no snmp-server community {public}  Impact: http://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-s2.html#GUID-2F3F13E4-EE81-4590-871D-6AE1043473DEhttp://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-s2.html#GUID-2F3F13E4-EE81-4590-871D-6AE1043473DE41   To reduce the risk of unauthorized access, Organizations should disable default, easy to guess, settings such as the 'public' setting for snmp-server community.  "
    # },
    # {
    #     "title": "1.5.4 Do not set 'RW' for any 'snmp-server community' (Scored) ",
    #     "description": "Specifies read-write access. Authorized management stations can both retrieve and modify MIB objects.  ",
    #     "audit": "Perform the following to determine if a read/write community string is enabled: Verify the result does not show a community string with a \"RW\" hostname#show run | incl snmp-server community  ",
    #     "command": "show run | incl snmp-server community",
    #     "recommendations": "Disable SNMP write access. hostname(config)#no snmp-server community {write_community_string}  Impact: To reduce the risk of unauthorized access, Organizations should disable the SNMP 'write' access for snmp-server community.  "
    # },
    # {
    #     "title": "1.5.5 Set the ACL for each 'snmp-server community' (Scored) ",
    #     "description": "This feature specifies a list of IP addresses that are allowed to use the community string to gain access to the SNMP agent.  ",
    #     "audit": "Perform the following to determine if an ACL is enabled: Verify the result shows a number after the community string hostname#show run | incl snmp-server community  ",
    #     "command": "show run | incl snmp-server community",
    #     "recommendations": "Configure authorized SNMP community string and restrict access to authorized management systems. hostname(config)#snmp-server community <community_string> ro {snmp_access-list_number |  snmp_access-list_name} Impact: To reduce the risk of unauthorized access, Organizations should enable access control lists for all snmp-server communities and restrict the access to appropriate trusted management zones. If possible, implement SNMPv3 to apply authentication, authorization, and data privatization (encryption) for additional benefits to the organization. http://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-s2.html#GUID-2F3F13E4-EE81-4590-871D-6AE1043473DEhttp://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-s2.html#GUID-2F3F13E4-EE81-4590-871D-6AE1043473DE43   Default Value: No ACL is set for SNMP  "
    # },
    # {
    #     "title": "1.5.6 Create an 'access-list' for use with SNMP (Scored) ",
    #     "description": "You can use access lists to control the transmission of packets on an interface, control Simple Network Management Protocol (SNMP) access, and restrict the contents of routing updates. The Cisco IOS software stops checking the extended access list after a match occurs.  ",
    #     "audit": "Perform the following to determine if the ACL is created: Verify you the appropriate access-list definitions hostname#sh ip access-list <snmp_acl_number>   ",
    #     "command": "sh ip access-list <snmp_acl_number> ",
    #     "recommendations": "Configure SNMP ACL for restricting access to the device from authorized management stations segmented in a trusted management zone. hostname(config)#access-list <snmp_acl_number> permit <snmp_access-list> hostname(config)#access-list deny any log  http://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-s2.html#GUID-2F3F13E4-EE81-4590-871D-6AE1043473DEhttp://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-s2.html#GUID-2F3F13E4-EE81-4590-871D-6AE1043473DE44   Default Value: SNMP does not use an access list.  "
    # },
    # {
    #     "title": "1.5.7 Set 'snmp-server host' when using SNMP (Scored) ",
    #     "description": "SNMP notifications can be sent as traps to authorized management systems.  ",
    #     "audit": "Perform the following to determine if SNMP traps are enabled: If the command returns configuration values, then SNMP is enabled. hostname#show run | incl snmp-server  ",
    #     "command": "show run | incl snmp-server",
    #     "recommendations": "Configure authorized SNMP trap community string and restrict sending messages to authorized management systems. hostname(config)#snmp-server host {ip_address} {trap_community_string} snmp  Impact: Organizations using SNMP should restrict sending SNMP messages only to explicitly named systems to reduce unauthorized access.  Default Value: A recipient is not specified to receive notifications. http://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-a2.html#GUID-9EA733A3-1788-4882-B8C3-AB0A2949120Chttp://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-a2.html#GUID-9EA733A3-1788-4882-B8C3-AB0A2949120C45    "
    # },
    # {
    #     "title": "1.5.8 Set 'snmp-server enable traps snmp' (Scored) ",
    #     "description": "SNMP notifications can be sent as traps to authorized management systems.   ",
    #     "audit": "Perform the following to determine if SNMP traps are enabled: If the command returns configuration values, then SNMP is enabled. hostname#show run | incl snmp-server  ",
    #     "command": "show run | incl snmp-server",
    #     "recommendations": "Enable SNMP traps. hostname(config)#snmp-server enable traps snmp authentication linkup linkdown coldstart  Impact: Organizations using SNMP should restrict trap types only to explicitly named traps to reduce unintended traffic. Enabling SNMP traps without specifying trap type will enable all SNMP trap types.  Default Value: SNMP notifications are disabled.  "
    # },
    # {
    #     "title": "1.5.9 Set 'priv' for each 'snmp-server group' using SNMPv3 (Scored) ",
    #     "description": "Specifies authentication of a packet with encryption when using SNMPv3  ",
    #     "audit": "Verify the result show the appropriate group name and security model hostname#show snmp groups  ",
    #     "command": "show snmp groups",
    #     "recommendations": "For each SNMPv3 group created on your router add privacy options by issuing the following command... hostname(config)#snmp-server group {group_name} v3 priv Impact: Organizations using SNMP can significantly reduce the risks of unauthorized access by using the 'snmp-server group v3 priv' setting to encrypt messages in transit. Default Value: No SNMP server groups are configured.  "
    # },
    # {
    #     "title": "1.5.10 Require 'aes 128' as minimum for 'snmp-server user' when using ",
    #     "description": "Specify the use of a minimum of 128-bit AES algorithm for encryption when using SNMPv3.  ",
    #     "audit": "Verify the result show the appropriate user name and security settings hostname#show snmp user  ",
    #     "command": "show snmp user",
    #     "recommendations": "For each SNMPv3 user created on your router add privacy options by issuing the following command. hostname(config)#snmp-server user {user_name} {group_name} v3 encrypted auth sha {auth_password} priv aes 128 {priv_password} {acl_name_or_number} Impact: Organizations using SNMP can significantly reduce the risks of unauthorized access by using the 'snmp-server user' setting with appropriate authentication and privacy protocols to encrypt messages in transit. Default Value: SNMP username as not set by default. http://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-s5.html#GUID-56E87D02-C56F-4E2D-A5C8-617E31740C3Fhttp://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-s5.html#GUID-56E87D02-C56F-4E2D-A5C8-617E31740C3F48    "
    # },
    # {
    #     "title": "2.1.1.1.1 Set the 'hostname' (Scored) ",
    #     "description": "The hostname is used in prompts and default configuration filenames.  ",
    #     "audit": "http://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-s5.html#GUID-4EED4031-E723-4B84-9BBF-610C3CF60E31http://www.cisco.com/en/US/docs/ios-xml/ios/snmp/command/nm-snmp-cr-s5.html#GUID-4EED4031-E723-4B84-9BBF-610C3CF60E3149   Perform the following to determine if the local time zone is configured: Verify the result shows the summer-time recurrence is configured properly. hostname#sh run | incl hostname  ",
    #     "command": "sh run | incl hostname",
    #     "recommendations": "Configure an appropriate host name for the router. hostname(config)#hostname {router_name} Impact: Organizations should plan the enterprise network and identify an appropriate host name for each router. Default Value: The default hostname is Router.  "
    # },
    # {
    #     "title": "2.1.1.1.2 Set the 'ip domain name' (Scored) ",
    #     "description": "Define a default domain name that the Cisco IOS software uses to complete unqualified hostnames  ",
    #     "audit": "Perform the following to determine if the domain name is configured: Verify the domain name is configured properly. http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/F_through_K.html#GUID-F3349988-EC16-484A-BE81-4C40110E6625http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/F_through_K.html#GUID-F3349988-EC16-484A-BE81-4C40110E6625http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/F_through_K.html#GUID-F3349988-EC16-484A-BE81-4C40110E662550   hostname#sh run | incl domain name  ",
    #     "command": "sh run | incl domain name",
    #     "recommendations": "Configure an appropriate domain name for the router. hostname (config)#ip domain name {domain-name} Impact: Organizations should plan the enterprise network and identify an appropriate domain name for the router. Default Value: No domain is set.  "
    # },
    # {
    #     "title": "2.1.1.1.3 Set 'modulus' to greater than or equal to 2048 for 'crypto key ",
    #     "description": "Use this command to generate RSA key pairs for your Cisco device. RSA keys are generated in pairs--one public RSA key and one private RSA key.  ",
    #     "audit": "Perform the following to determine if the RSA key pair is configured:  hostname#sh crypto key mypubkey rsa http://www.cisco.com/en/US/docs/ios-xml/ios/ipaddr/command/ipaddr-i3.html#GUID-A706D62B-9170-45CE-A2C2-7B2052BE2CABhttp://www.cisco.com/en/US/docs/ios-xml/ios/ipaddr/command/ipaddr-i3.html#GUID-A706D62B-9170-45CE-A2C2-7B2052BE2CAB51    ",
    #     "command": "sh crypto key mypubkey rsa",
    #     "recommendations": "Generate an RSA key pair for the router. hostname(config)#crypto key generate rsa general-keys modulus 2048 Impact: Organizations should plan and implement enterprise network cryptography and generate an appropriate RSA key pairs, such as 'modulus', greater than or equal to 2048. Default Value: RSA key pairs do not exist.  "
    # },
    # {
    #     "title": "2.1.1.1.4 Set 'seconds' for 'ip ssh timeout' (Scored) ",
    #     "description": "The time interval that the router waits for the SSH client to respond before disconnecting an uncompleted login attempt.  ",
    #     "audit": "Perform the following to determine if the SSH timeout is configured: Verify the timeout is configured properly. hostname#sh ip ssh http://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-c4.html#GUID-2AECF701-D54A-404E-9614-D3AAB049BC13http://www.cisco.com/en/US/docs/ios-xml/ios/security/a1/sec-cr-c4.html#GUID-2AECF701-D54A-404E-9614-D3AAB049BC1352    ",
    #     "command": "sh ip ssh",
    #     "recommendations": "Configure the SSH timeout hostname(config)#ip ssh time-out [60]  Impact: Organizations should implement a security policy requiring minimum timeout settings for all network administrators and enforce the policy through the 'ip ssh timeout' command. Default Value: SSH in not enabled by default.  "
    # },
    # {
    #     "title": "2.1.1.1.5 Set maximimum value for 'ip ssh authentication-retries' ",
    #     "description": "The number of retries before the SSH login session disconnects.  ",
    #     "audit": "Perform the following to determine if SSH authentication retries is configured: Verify the authentication retries is configured properly. hostname#sh ip ssh http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i3.html#GUID-5BAC7A2B-0A25-400F-AEE9-C22AE08513C6http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i3.html#GUID-5BAC7A2B-0A25-400F-AEE9-C22AE08513C653    ",
    #     "command": "sh ip ssh",
    #     "recommendations": "Configure the SSH timeout: hostname(config)#ip ssh authentication-retries [3] Impact: Organizations should implement a security policy limiting the number of authentication attempts for network administrators and enforce the policy through the 'ip ssh authentication-retries' command. Default Value: SSH is not enabled by default.  When set, the default value is 3.  "
    # },
    # {
    #     "title": "2.1.1.2 Set version 2 for 'ip ssh version' (Scored) ",
    #     "description": "Specify the version of Secure Shell (SSH) to be run on a router  ",
    #     "audit": "Perform the following to determine if SSH version 2 is configured: Verify that SSH version 2 is configured properly. http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i3.html#GUID-5BAC7A2B-0A25-400F-AEE9-C22AE08513C6http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i3.html#GUID-5BAC7A2B-0A25-400F-AEE9-C22AE08513C654   hostname#sh ip ssh  ",
    #     "command": "sh ip ssh",
    #     "recommendations": "Configure the router to use SSH version 2 hostname(config)#ip ssh version 2 Impact: To reduce the risk of unauthorized access, organizations should implement a security policy to review their current protocols to ensure the most secure protocol versions are in use. Default Value: SSH is not enabled by default.  When enabled, SSH operates in compatibility mode (versions 1 and 2 supported).  "
    # },
    # {
    #     "title": "2.1.2 Set 'no cdp run' (Scored) ",
    #     "description": "Disable Cisco Discovery Protocol (CDP) service at device level.  ",
    #     "audit": "Perform the following to determine if CDP is enabled: http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i3.html#GUID-170AECF1-4B5B-462A-8CC8-999DEDC45C21http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i3.html#GUID-170AECF1-4B5B-462A-8CC8-999DEDC45C2155   Verify the result shows \"CDP is not enabled\" hostname#show cdp  ",
    #     "command": "show cdp",
    #     "recommendations": "Disable Cisco Discovery Protocol (CDP) service globally. hostname(config)#no cdp run Impact: To reduce the risk of unauthorized access, organizations should implement a security policy restricting network protocols and explicitly require disabling all insecure or unnecessary protocols. Default Value: Enabled on all platforms except the Cisco 10000 Series Edge Services Router  "
    # },
    # {
    #     "title": "2.1.3 Set 'no ip bootp server' (Scored) ",
    #     "description": "Disable the Bootstrap Protocol (BOOTP) service on your routing device.  ",
    #     "audit": "Perform the following to determine if bootp is enabled: Verify a \"no ip bootp server\" result returns hostname#show run | incl bootp http://www.cisco.com/en/US/docs/ios-xml/ios/cdp/command/cdp-cr-a1.html#GUID-E006FAC8-417E-4C3F-B732-4D47B0447750http://www.cisco.com/en/US/docs/ios-xml/ios/cdp/command/cdp-cr-a1.html#GUID-E006FAC8-417E-4C3F-B732-4D47B044775056    ",
    #     "command": "show run | incl bootp ",
    #     "recommendations": "Disable the bootp server. hostname(config)#no ip bootp server Impact: To reduce the risk of unauthorized access, organizations should implement a security policy restricting network protocols and explicitly require disabling all insecure or unnecessary protocols such as 'ip bootp server'. Default Value: Enabled  "
    # },
    # {
    #     "title": "2.1.4 Set 'no service dhcp' (Scored) ",
    #     "description": "Disable the Dynamic Host Configuration Protocol (DHCP) server and relay agent features on your router.  ",
    #     "audit": "Perform the following to determine if the DHCP service is enabled: Verify no result returns hostname#show run | incl dhcp 57    ",
    #     "command": "show run | incl dhcp 57 ",
    #     "recommendations": "Disable the DHCP server. hostname(config)#no service dhcp Impact: To reduce the risk of unauthorized access, organizations should implement a security policy restricting network protocols and explicitly require disabling all insecure or unnecessary protocols such as the Dynamic Host Configuration Protocol (DHCP). Default Value: Enabled by default, but also requires a DHCP pool to be set to activate the DHCP server.  "
    # },
    # {
    #     "title": "2.1.5 Set 'no ip identd' (Scored) ",
    #     "description": "Disable the identification (identd) server.  ",
    #     "audit": "Perform the following to determine if identd is enabled: Verify no result returns hostname#show run | incl identd  ",
    #     "command": "show run | incl identd ",
    #     "recommendations": "http://www.cisco.com/en/US/docs/ios-xml/ios/ipaddr/command/ipaddr-r1.html#GUID-1516B259-AA28-4839-B968-8DDBF0B382F6http://www.cisco.com/en/US/docs/ios-xml/ios/ipaddr/command/ipaddr-r1.html#GUID-1516B259-AA28-4839-B968-8DDBF0B382F658   Disable the ident server. hostname(config)#no ip identd Impact: To reduce the risk of unauthorized access, organizations should implement a security policy restricting network protocols and explicitly require disabling all insecure or unnecessary protocols such as the identification protocol (identd). Default Value: Enabled by default  "
    # },
    # {
    #     "title": "2.1.6 Set 'service tcp-keepalives-in' (Scored) ",
    #     "description": "Generate keepalive packets on idle incoming network connections.  ",
    #     "audit": "Perform the following to determine if the feature is enabled: Verify a command string result returns hostname#show run | incl service tcp http://www.cisco.com/en/US/docs/solutions/Enterprise/Security/Baseline_Security/sec_chap4.html#wp1056539http://www.cisco.com/en/US/docs/solutions/Enterprise/Security/Baseline_Security/sec_chap4.html#wp105653959    ",
    #     "command": "show run | incl service tcp ",
    #     "recommendations": "Enable TCP keepalives-in service: hostname(config)#service tcp-keepalives-in Impact: To reduce the risk of unauthorized access, organizations should implement a security policy restricting how long to allow terminated sessions and enforce this policy through the use of 'tcp-keepalives-in' command. Default Value: Disabled by default.  "
    # },
    # {
    #     "title": "2.1.7 Set 'service tcp-keepalives-out' (Scored) ",
    #     "description": "Generate keepalive packets on idle outgoing network connections.  ",
    #     "audit": "Perform the following to determine if the feature is enabled: Verify a command string result returns http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/R_through_setup.html#GUID-1489ABA3-2428-4A64-B252-296A035DB85Ehttp://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/R_through_setup.html#GUID-1489ABA3-2428-4A64-B252-296A035DB85Ehttp://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/R_through_setup.html#GUID-1489ABA3-2428-4A64-B252-296A035DB85E60   hostname#show run | incl service tcp  ",
    #     "command": "show run | incl service tcp ",
    #     "recommendations": "Enable TCP keepalives-out service: hostname(config)#service tcp-keepalives-out Impact: To reduce the risk of unauthorized access, organizations should implement a security policy restricting how long to allow terminated sessions and enforce this policy through the use of 'tcp-keepalives-out' command. Default Value: Disabled by default.  "
    # },
    # {
    #     "title": "2.1.8 Set 'no service pad' (Scored) ",
    #     "description": "Disable X.25 Packet Assembler/Disassembler (PAD) service.  ",
    #     "audit": "Perform the following to determine if the feature is disabled: Verify no result returns hostname#show run | incl service pad http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/R_through_setup.html#GUID-9321ECDC-6284-4BF6-BA4A-9CEEF5F993E5http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/R_through_setup.html#GUID-9321ECDC-6284-4BF6-BA4A-9CEEF5F993E5http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/R_through_setup.html#GUID-9321ECDC-6284-4BF6-BA4A-9CEEF5F993E561    ",
    #     "command": "show run | incl service pad ",
    #     "recommendations": "Disable the PAD service. hostname(config)#no service pad Impact: To reduce the risk of unauthorized access, organizations should implement a security policy restricting unnecessary services such as the 'PAD' service. Default Value: Enabled by default.  "
    # },
    # {
    #     "title": "2.2.1 Set 'logging on' (Scored) ",
    #     "description": "Enable logging of system messages.  ",
    #     "audit": "Perform the following to determine if the feature is enabled: Verify no result returns http://www.cisco.com/en/US/docs/ios-xml/ios/wan/command/wan-s1.html#GUID-C5497B77-3FD4-4D2F-AB08-1317D5F5473Bhttp://www.cisco.com/en/US/docs/ios-xml/ios/wan/command/wan-s1.html#GUID-C5497B77-3FD4-4D2F-AB08-1317D5F5473B62   hostname#show run | incl logging on  ",
    #     "command": "show run | incl logging on",
    #     "recommendations": "Enable system logging. hostname(config)#logging on Impact: Enabling the Cisco IOS 'logging on' command enforces the monitoring of technology risks for the organizations' network devices. Default Value: Logging is not enabled.  "
    # },
    # {
    #     "title": "2.2.2 Set 'buffer size' for 'logging buffered' (Scored) ",
    #     "description": "Enable system message logging to a local buffer.  ",
    #     "audit": "Perform the following to determine if the feature is enabled: Verify a command string result returns hostname#show run | incl logging buffered  ",
    #     "command": "show run | incl logging buffered",
    #     "recommendations": "http://www.cisco.com/en/US/docs/ios/netmgmt/command/reference/nm_09.html#wp1014324http://www.cisco.com/en/US/docs/ios/netmgmt/command/reference/nm_09.html#wp101432463   Configure buffered logging (with minimum size). Recommended size is 64000. hostname(config)#logging buffered [log_buffer_size] Impact: Data forensics is effective for managing technology risks and an organization can enforce such policies by enabling the 'logging buffered' command. Default Value: No logging buffer is set by default  "
    # },
    # {
    #     "title": "2.2.4 Set IP address for 'logging host' (Scored) ",
    #     "description": "Log system messages and debug output to a remote host.  ",
    #     "audit": "Perform the following to determine if a syslog server is enabled: Verify one or more IP address(es) returns hostname#sh log | incl logging host  ",
    #     "command": "sh log | incl logging host",
    #     "recommendations": "Designate one or more syslog servers by IP address. 65   hostname(config)#logging host syslog_server Impact: Logging is an important process for an organization managing technology risk. The 'logging host' command sets the IP address of the logging host and enforces the logging process. Default Value: System logging messages are not sent to any remote host.  "
    # },
    # {
    #     "title": "2.2.5 Set 'logging trap informational' (Scored) ",
    #     "description": "Limit messages logged to the syslog servers based on severity level informational.  ",
    #     "audit": "Perform the following to determine if a syslog server for SNMP traps is enabled: Verify \"level informational\" returns hostname#sh log | incl trap logging  ",
    #     "command": "sh log | incl trap logging",
    #     "recommendations": "Configure SNMP trap and syslog logging level. hostname(config)#logging trap informational Impact: http://www.cisco.com/en/US/docs/ios/netmgmt/command/reference/nm_09.html#wp1082864http://www.cisco.com/en/US/docs/ios/netmgmt/command/reference/nm_09.html#wp108286466   Logging is an important process for an organization managing technology risk. The 'logging trap' command sets the severity of messages and enforces the logging process. Default Value: Disabled  "
    # },
    # {
    #     "title": "2.2.6 Set 'service timestamps debug datetime' (Scored) ",
    #     "description": "Configure the system to apply a time stamp to debugging messages or system logging messages  ",
    #     "audit": "Perform the following to determine if the additional detail is enabled: Verify a command string result returns hostname#sh run | incl service timestamps  ",
    #     "command": "sh run | incl service timestamps",
    #     "recommendations": "Configure debug messages to include timestamps. hostname(config)#service timestamps debug datetime {msec} show-timezone Impact: http://www.cisco.com/en/US/docs/ios/netmgmt/command/reference/nm_09.html#wp1015177http://www.cisco.com/en/US/docs/ios/netmgmt/command/reference/nm_09.html#wp101517767   Logging is an important process for an organization managing technology risk and establishing a timeline of events is critical. The 'service timestamps' command sets the date and time on entries sent to the logging host and enforces the logging process. Default Value: Time stamps are applied to debug and logging messages.  "
    # },
    # {
    #     "title": "2.2.7 Set 'logging source interface' (Scored) ",
    #     "description": "Specify the source IPv4 or IPv6 address of system logging packets  ",
    #     "audit": "Perform the following to determine if logging services are bound to a source interface: Verify a command string result returns hostname#sh run | incl logging source  ",
    #     "command": "sh run | incl logging source",
    #     "recommendations": "Bind logging to the loopback interface. hostname(config)#logging source-interface loopback {loopback_interface_number} Impact: http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/R_through_setup.html#GUID-DC110E59-D294-4E3D-B67F-CCB06E607FC6http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/R_through_setup.html#GUID-DC110E59-D294-4E3D-B67F-CCB06E607FC6http://www.cisco.com/en/US/docs/ios-xml/ios/fundamentals/command/R_through_setup.html#GUID-DC110E59-D294-4E3D-B67F-CCB06E607FC668   Logging is an important process for an organization managing technology risk and establishing a consistent source of messages for the logging host is critical. The 'logging source interface loopback' command sets a consistent IP address to send messages to the logging host and enforces the logging process. Default Value: The wildcard interface address is used.  "
    # },
    # {
    #     "title": "2.3.1.1 Set 'ntp authenticate' (Scored) ",
    #     "description": "Enable NTP authentication.  ",
    #     "audit": "From the command prompt, execute the following commands: hostname#show run | include ntp  http://www.cisco.com/en/US/docs/ios/netmgmt/command/reference/nm_09.html#wp1095099http://www.cisco.com/en/US/docs/ios/netmgmt/command/reference/nm_09.html#wp109509969    ",
    #     "command": "show run | include ntp "
    # },
    # {
    #     "title": "2.3.1.2 Set 'ntp authentication-key' (Scored) ",
    #     "description": "Define an authentication key for Network Time Protocol (NTP).  ",
    #     "audit": "From the command prompt, execute the following commands: hostname#show run | include ntp authentication-key  ",
    #     "command": "show run | include ntp authentication-key  ",
    #     "recommendations": "Configure at the NTP key ring and encryption key using the following command hostname(config)#ntp authentication-key {ntp_key_id} md5 {ntp_key} http://www.cisco.com/en/US/docs/ios-xml/ios/bsm/command/bsm-cr-n1.html#GUID-8BEBDAF4-6D03-4C3E-B8D6-6BCBC7D0F324http://www.cisco.com/en/US/docs/ios-xml/ios/bsm/command/bsm-cr-n1.html#GUID-8BEBDAF4-6D03-4C3E-B8D6-6BCBC7D0F32470   Impact: Organizations should establish three Network Time Protocol (NTP) hosts to set consistent time across the enterprise.  Enabling the 'ntp authentication-key' command enforces encrypted authentication between NTP hosts. Default Value: No authentication key is defined for NTP.  "
    # },
    # {
    #     "title": "2.3.1.3 Set the 'ntp trusted-key' (Scored) ",
    #     "description": "Ensure you authenticate the identity of a system to which Network Time Protocol (NTP) will synchronize  ",
    #     "audit": "From the command prompt, execute the following commands: hostname#show run | include ntp trusted-key  The above command should return any NTP server(s) configured with encryption keys. This value should be the same as the total number of servers configured as tested in. http://www.cisco.com/en/US/docs/ios-xml/ios/bsm/command/bsm-cr-n1.html#GUID-0435BFD1-D7D7-41D4-97AC-7731C11226BChttp://www.cisco.com/en/US/docs/ios-xml/ios/bsm/command/bsm-cr-n1.html#GUID-0435BFD1-D7D7-41D4-97AC-7731C11226BC71    ",
    #     "command": "show run | include ntp trusted-key  ",
    #     "recommendations": "Configure the NTP trusted key using the following command hostname(config)#ntp trusted-key {ntp_key_id} Impact: Organizations should establish three Network Time Protocol (NTP) hosts to set consistent time across the enterprise.  Enabling the 'ntp trusted-key' command enforces encrypted authentication between NTP hosts. Default Value: Authentication of the identity of the system is disabled.  "
    # },
    # {
    #     "title": "2.3.2 Set 'ip address' for 'ntp server' (Scored) ",
    #     "description": "Use this command if you want to allow the system to synchronize the system software clock with the specified NTP server.  ",
    #     "audit": "From the command prompt, execute the following commands: hostname#sh ntp associations  ",
    #     "command": "sh ntp associations ",
    #     "recommendations": "Configure at least one external NTP Server using the following commands hostname(config)#ntp server {ip address} Impact: 73   Organizations should establish three Network Time Protocol (NTP) hosts to set consistent time across the enterprise.  Enabling the 'ntp server ip address' enforces encrypted authentication between NTP hosts. Default Value: No servers are configured by default.  "
    # },
    # {
    #     "title": "2.4.1 Create a single 'interface loopback' (Scored) ",
    #     "description": "Configure a single loopback interface.  ",
    #     "audit": "Perform the following to determine if a loopback interface is defined: http://www.cisco.com/en/US/docs/ios-xml/ios/bsm/command/bsm-cr-n1.html#GUID-255145EB-D656-43F0-B361-D9CBCC794112http://www.cisco.com/en/US/docs/ios-xml/ios/bsm/command/bsm-cr-n1.html#GUID-255145EB-D656-43F0-B361-D9CBCC79411274   Verify an IP address returns for the defined loopback interface hostname#sh ip int brief | incl Loopback  ",
    #     "command": "sh ip int brief | incl Loopback  ",
    #     "recommendations": "Define and configure one loopback interface. hostname(config)#interface loopback <number> hostname(config-if)#ip address <loopback_ip_address> <loopback_subnet_mask>  Impact: Organizations should plan and establish 'loopback interfaces' for the enterprise network. Loopback interfaces enable critical network information such as OSPF Router IDs and provide termination points for routing protocol sessions. Default Value: There are no loopback interfaces defined by default.  "
    # },
    # {
    #     "title": "2.4.2 Set AAA 'source-interface' (Scored) ",
    #     "description": "Force AAA to use the IP address of a specified interface for all outgoing AAA packets  ",
    #     "audit": "Perform the following to determine if AAA services are bound to a source interface: Verify a command string result returns http://www.cisco.com/en/US/docs/ios-xml/ios/interface/command/ir-i1.html#GUID-0D6BDFCD-3FBB-4D26-A274-C1221F8592DFhttp://www.cisco.com/en/US/docs/ios-xml/ios/interface/command/ir-i1.html#GUID-0D6BDFCD-3FBB-4D26-A274-C1221F8592DF75   hostname#sh run | incl tacacs source | radius source  ",
    #     "command": "sh run | incl tacacs source | radius source  ",
    #     "recommendations": "Bind AAA services to the loopback interface. Hostname(config)#ip {tacacs|radius} source-interface loopback {loopback_interface_number) Impact: Organizations should design and implement authentication, authorization, and accounting (AAA) services for effective monitoring of enterprise network devices. Binding AAA services to the source-interface loopback enables these services.  "
    # },
    # {
    #     "title": "2.4.3 Set 'ntp source' to Loopback Interface (Scored) ",
    #     "description": "Use a particular source address in Network Time Protocol (NTP) packets.  ",
    #     "audit": "Perform the following to determine if NTP services are bound to a source interface: Verify a command string result returns hostname#sh run | incl ntp source  ",
    #     "command": "sh run | incl ntp source  ",
    #     "recommendations": "http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i2.html#GUID-22E8B211-751F-48E0-9C76-58F0FE0AABA8http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i2.html#GUID-22E8B211-751F-48E0-9C76-58F0FE0AABA8http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i3.html#GUID-54A00318-CF69-46FC-9ADC-313BFC436713http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i3.html#GUID-54A00318-CF69-46FC-9ADC-313BFC43671376   Bind the NTP service to the loopback interface. hostname(config)#ntp source loopback {loopback_interface_number} Impact: Organizations should plan and implement network time protocol (NTP) services to establish official time for all enterprise network devices. Setting 'ntp source loopback' enforces the proper IP address for NTP services.  Default Value: Source address is determined by the outgoing interface.  "
    # },
    # {
    #     "title": "2.4.4 Set 'ip tftp source-interface' to the Loopback Interface (Scored) ",
    #     "description": "Specify the IP address of an interface as the source address for TFTP connections.  ",
    #     "audit": "Perform the following to determine if TFTP services are bound to a source interface: Verify a command string result returns hostname#sh run | incl tftp source-interface  ",
    #     "command": "sh run | incl tftp source-interface ",
    #     "recommendations": "Bind the TFTP client to the loopback interface. hostname(config)#ip tftp source-interface loopback {loobpback_interface_number} http://www.cisco.com/en/US/docs/ios-xml/ios/bsm/command/bsm-cr-n1.html#GUID-DF29FBFB-E1C0-4E5C-9013-D4CE59CA0B88http://www.cisco.com/en/US/docs/ios-xml/ios/bsm/command/bsm-cr-n1.html#GUID-DF29FBFB-E1C0-4E5C-9013-D4CE59CA0B8877   Impact: Organizations should plan and implement trivial file transfer protocol (TFTP) services in the enterprise by setting 'tftp source-interface loopback', which enables the TFTP servers to identify routers and authenticate requests by IP address. Default Value: The address of the closest interface to the destination is selected as the source address.  "
    # },
    # {
    #     "title": "3.1.1 Set 'no ip source-route' (Scored) ",
    #     "description": "Disable the handling of IP datagrams with source routing header options.  ",
    #     "audit": "Verify the command string result returns hostname#sh run | incl ip source-route  ",
    #     "command": "sh run | incl ip source-route  ",
    #     "recommendations": "Disable source routing. hostname(config)#no ip source-route Impact: Organizations should plan and implement network policies to ensure unnecessary services are explicitly disabled. The 'ip source-route' feature has been used in several attacks and should be disabled.  Default Value: Enabled by default  "
    # },
    # {
    #     "title": "3.1.2 Set 'no ip proxy-arp' (Scored) ",
    #     "description": "Disable proxy ARP on all interfaces.  ",
    #     "audit": "Verify the proxy ARP status hostname#sh ip int <interface> | incl proxy-arp   ",
    #     "command": "sh ip int <interface> | incl proxy-arp   ",
    #     "recommendations": "Disable proxy ARP on all interfaces. hostname(config)#interface <interface> hostname(config-if)#no ip proxy-arp Impact: Organizations should plan and implement network policies to ensure unnecessary services are explicitly disabled. The 'ip proxy-arp' feature effectively breaks the LAN security perimeter and should be disabled. Default Value: Enabled  "
    # },
    # {
    #     "title": "3.1.3 Set 'no interface tunnel' (Scored) ",
    #     "description": "Verify no tunnel interfaces are defined.  ",
    #     "audit": "Verify no tunnel interfaces are defined hostname#sh ip int brief | incl tunnel   ",
    #     "command": "sh ip int brief | incl tunnel   ",
    #     "recommendations": "Remove any tunnel interfaces. hostname(config)#no interface tunnel {instance} Impact: Organizations should plan and implement enterprise network security policies that disable insecure and unnecessary features that increase attack surfaces such as 'tunnel interfaces'. Default Value: No tunnel interfaces are defined  "
    # },
    # {
    #     "title": "3.1.4 Set 'ip verify unicast source reachable-via' (Scored) ",
    #     "description": "http://www.cisco.com/en/US/docs/ios-xml/ios/interface/command/ir-i1.html#GUID-0D6BDFCD-3FBB-4D26-A274-C1221F8592DFhttp://www.cisco.com/en/US/docs/ios-xml/ios/interface/command/ir-i1.html#GUID-0D6BDFCD-3FBB-4D26-A274-C1221F8592DF81   Examines incoming packets to determine whether the source address is in the Forwarding Information Base (FIB) and permits the packet only if the source is reachable through the interface on which the packet was received (sometimes referred to as strict mode).  ",
    #     "audit": "Verify uRPF is running on the appropriate interface(s) hostname#sh ip int <interface> | incl verify source   ",
    #     "command": "sh ip int <interface> | incl verify source   ",
    #     "recommendations": "Configure uRPF. hostname(config)#interface <interface_name> hostname(config-if)#ip verify unicast source reachable-via rx  Impact: Organizations should plan and implement enterprise security policies that protect the confidentiality, integrity, and availability of network devices. The 'unicast Reverse-Path Forwarding' (uRPF) feature dynamically uses the router table to either accept or drop packets when arriving on an interface. Default Value: Unicast RPF is disabled.  "
    # },
    # {
    #     "title": "3.2.1 Set 'ip access-list extended' to Forbid Private Source Addresses ",
    #     "description": "This command places the router in access-list configuration mode, where you must define the denied or permitted access conditions by using the deny and permit commands.  ",
    #     "audit": "Verify you have the appropriate access-list definitions hostname#sh ip access-list {name | number}  ",
    #     "command": "sh ip access-list {name | number}  ",
    #     "recommendations": "Configure ACL for private source address restrictions from external networks. hostname(config)#ip access-list extended {name | number}  hostname(config-nacl)#deny ip {internal_networks} any log hostname(config-nacl)#deny ip 127.0.0.0 0.255.255.255 any log hostname(config-nacl)#deny ip 10.0.0.0 0.255.255.255 any log hostname(config-nacl)#deny ip 0.0.0.0 0.255.255.255 any log hostname(config-nacl)#deny ip 172.16.0.0 0.15.255.255 any log hostname(config-nacl)#deny ip 192.168.0.0 0.0.255.255 any log hostname(config-nacl)#deny ip 192.0.2.0 0.0.0.255 any log hostname(config-nacl)#deny ip 169.254.0.0 0.0.255.255 any log 83   hostname(config-nacl)#deny ip 224.0.0.0 31.255.255.255 any log hostname(config-nacl)#deny ip host 255.255.255.255 any log hostname(config-nacl)#permit {protocol} {source_ip} {source_mask} {destination} {destination_mask} log hostname(config-nacl)#deny any any log hostname(config)#interface <external_interface> hostname(config-if)#access-group <access-list> in Impact: Organizations should plan and implement enterprise security policies that explicitly separate internal from external networks. Adding 'ip access-list' explicitly permitting and denying internal and external networks enforces these policies. Default Value: No access list defined  "
    # },
    # {
    #     "title": "3.2.2 Set inbound 'ip access-group' on the External Interface (Not Scored) ",
    #     "description": "This command places the router in access-list configuration mode, where you must define the denied or permitted access conditions by using the deny and permit commands.  ",
    #     "audit": "Verify the access-group is applied to the appropriate interface http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i1.html#GUID-BD76E065-8EAC-4B32-AF25-04BA94DD2B11http://www.cisco.com/en/US/docs/ios-xml/ios/security/d1/sec-cr-i1.html#GUID-BD76E065-8EAC-4B32-AF25-04BA94DD2B1184   hostname#sh run | sec interface <external_interface>  ",
    #     "command": "sh run | sec interface <external_interface>  ",
    #     "recommendations": "Apply the access-group for the external (untrusted) interface hostname(config)#interface <external_interface> hostname(config-if)#ip access-group {name | number} in Impact: Organizations should plan and implement enterprise security policies explicitly permitting and denying access based upon access lists.  Using the 'ip access-group' command enforces these policies by explicitly identifying groups permitted access. Default Value: No access-group defined  "
    # },
    # {
    #     "title": "3.3.1.1 Set 'key chain' (Scored) ",
    #     "description": "Define an authentication key chain to enable authentication for routing protocols. A key chain must have at least one key and can have up to 2,147,483,647 keys. NOTE: Only DRP Agent, EIGRP, and RIPv2 use key chains.  ",
    #     "audit": "Verify the appropriate key chain is defined hostname#sh run | sec key chain   ",
    #     "command": "sh run | sec key chain   ",
    #     "recommendations": "Establish the key chain. hostname(config)#key chain {key-chain_name} Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Using 'key chains' for routing protocols enforces these policies. Default Value: 86   Not set  "
    # },
    # {
    #     "title": "3.3.1.2 Set 'key' (Scored) ",
    #     "description": "Configure an authentication key on a key chain.  ",
    #     "audit": "Verify the appropriate key chain is defined hostname#sh run | sec key chain   ",
    #     "command": "sh run | sec key chain   ",
    #     "recommendations": "Configure the key number. hostname(config-keychain)#key {key-number} Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Using 'key numbers' for key chains for routing protocols enforces these policies.  "
    # },
    # {
    #     "title": "3.3.1.3 Set 'key-string' (Scored) ",
    #     "description": "Configure the authentication string for a key.  ",
    #     "audit": "Verify the appropriate key chain is defined hostname#sh run | sec key chain   ",
    #     "command": "sh run | sec key chain   ",
    #     "recommendations": "Configure the key string. hostname(config-keychain-key)#key-string <key-string>  Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Using 'key strings' for key chains for routing protocols enforces these policies. Default Value: Not set  "
    # },
    # {
    #     "title": "3.3.1.4 Set 'address-family ipv4 autonomous-system' (Scored) ",
    #     "description": "Configure the EIGRP address family.  ",
    #     "audit": "Verify the appropriate address family is set hostname#sh run | sec router eigrp   ",
    #     "command": "sh run | sec router eigrp   ",
    #     "recommendations": "Configure the EIGRP address family. hostname(config)#router eigrp <virtual-instance-name> hostname(config-router)#address-family ipv4 autonomous-system {eigrp_as-number} Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Using 'address-family' for EIGRP enforces these policies by restricting the exchanges between predefined network devices. Default Value: Not set  "
    # },
    # {
    #     "title": "3.3.1.5 Set 'af-interface default' (Scored) ",
    #     "description": "http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-i1.html#GUID-67388D6C-AE9C-47CA-8C35-2A2CF9FA668Ehttp://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-i1.html#GUID-67388D6C-AE9C-47CA-8C35-2A2CF9FA668Ehttp://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-a1.html#GUID-C03CFC8A-3CE3-4CF9-9D65-52990DBD3377http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-a1.html#GUID-C03CFC8A-3CE3-4CF9-9D65-52990DBD337789   Defines user defaults to apply to EIGRP interfaces that belong to an address-family.  ",
    #     "audit": "Verify the setting hostname#sh run | sec router eigrp   ",
    #     "command": "sh run | sec router eigrp   ",
    #     "recommendations": "Configure the EIGRP address family. hostname(config)#router eigrp <virtual-instance-name> hostname(config-router)#address-family ipv4 autonomous-system {eigrp_as-number} hostname(config-router-af)#af-interface default  Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Using 'af-interface default' for EIGRP interfaces enforces these policies by restricting the exchanges between predefined network devices. Default Value: Not set  "
    # },
    # {
    #     "title": "3.3.1.6 Set 'authentication key-chain' (Scored) ",
    #     "description": "http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-i1.html#GUID-67388D6C-AE9C-47CA-8C35-2A2CF9FA668Ehttp://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-i1.html#GUID-67388D6C-AE9C-47CA-8C35-2A2CF9FA668Ehttp://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-a1.html#GUID-C03CFC8A-3CE3-4CF9-9D65-52990DBD3377http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-a1.html#GUID-C03CFC8A-3CE3-4CF9-9D65-52990DBD3377http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-a1.html#GUID-DC0EF1D3-DFD4-45DF-A553-FA432A3E7233http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-a1.html#GUID-DC0EF1D3-DFD4-45DF-A553-FA432A3E723390   Configure the EIGRP address family key chain.  ",
    #     "audit": "Verify the appropriate key chain is set hostname#sh run | sec router eigrp   ",
    #     "command": "sh run | sec router eigrp   ",
    #     "recommendations": "Configure the EIGRP address family key chain. hostname(config)#router eigrp <virtual-instance-name> hostname(config-router)#address-family ipv4 autonomous-system {eigrp_as-number} hostname(config-router-af)#af-interface {interface-name} hostname(config-router-af-interface)#authentication key-chain {eigrp_key-chain_name} Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Using the address-family 'key chain' for EIGRP enforces these policies by restricting the exchanges between predefined network devices. Default Value: No key chains are specified for EIGRP  "
    # },
    # {
    #     "title": "3.3.1.7 Set 'authentication mode md5' (Scored) ",
    #     "description": "Configure authentication to prevent unapproved sources from introducing unauthorized or false service messages.  ",
    #     "audit": "Verify the appropriate address family authentication mode is set hostname#sh run | sec router eigrp   ",
    #     "command": "sh run | sec router eigrp   ",
    #     "recommendations": "Configure the EIGRP address family authentication mode. hostname(config)#router eigrp <virtual-instance-name> hostname(config-router)#address-family ipv4 autonomous-system {eigrp_as-number} hostname(config-router-af)#af-interface {interface-name} hostname(config-router-af-interface)#authentication mode md5 Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Using the 'authentication mode' for EIGRP address-family or service-family packets enforces these policies by restricting the type of authentication between network devices. Default Value: Not defined  "
    # },
    # {
    #     "title": "3.3.1.8 Set 'ip authentication key-chain eigrp' (Scored) ",
    #     "description": "Specify the type of authentication used in Enhanced Interior Gateway Routing Protocol (EIGRP) packets per interface.  ",
    #     "audit": "Verify the appropriate key chain is set on the appropriate interface(s) hostname#sh run int <interface_name> | incl key-chain   ",
    #     "command": "sh run int <interface_name> | incl key-chain   ",
    #     "recommendations": "Configure the interface with the EIGRP key chain. hostname(config)#interface <interface_name> hostname(config-if)#ip authentication key-chain eigrp {eigrp_as-number} {eigrp_key-chain_name} Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Configuring the interface with 'ip authentication key chain' for EIGRP by name and number enforces these policies by restricting the exchanges between network devices. Default Value: Not set http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-a1.html#GUID-C03CFC8A-3CE3-4CF9-9D65-52990DBD3377http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-a1.html#GUID-C03CFC8A-3CE3-4CF9-9D65-52990DBD3377http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-a1.html#GUID-A29E0EF6-4CEF-40A7-9824-367939001B73http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-a1.html#GUID-A29E0EF6-4CEF-40A7-9824-367939001B7393    "
    # },
    # {
    #     "title": "3.3.1.9 Set 'ip authentication mode eigrp' (Scored) ",
    #     "description": "Configure authentication to prevent unapproved sources from introducing unauthorized or false routing messages.  ",
    #     "audit": "Verify the appropriate authentication mode is set on the appropriate interface(s) hostname#sh run int <interface_name> | incl authentication mode  ",
    #     "command": "sh run int <interface_name> | incl authentication mode  ",
    #     "recommendations": "Configure the interface with the EIGRP authentication mode. hostname(config)#interface <interface_name> hostname(config-if)#ip authentication mode eigrp {eigrp_as-number} md5 Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Configuring the interface with 'ip authentication mode' for EIGRP by number and mode enforces these policies by restricting the exchanges between network devices. Default Value: Not set http://www.cisco.com/en/US/docs/ios-xml/ios/interface/command/ir-i1.html#GUID-0D6BDFCD-3FBB-4D26-A274-C1221F8592DFhttp://www.cisco.com/en/US/docs/ios-xml/ios/interface/command/ir-i1.html#GUID-0D6BDFCD-3FBB-4D26-A274-C1221F8592DFhttp://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-i1.html#GUID-0B344B46-5E8E-4FE2-A3E0-D92410CE5E91http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-i1.html#GUID-0B344B46-5E8E-4FE2-A3E0-D92410CE5E9194    "
    # },
    # {
    #     "title": "3.3.2.1 Set 'authentication message-digest' for OSPF area (Scored) ",
    #     "description": "Enable MD5 authentication for OSPF.  ",
    #     "audit": "Verify message digest for OSPF is defined hostname#sh run | sec router ospf   ",
    #     "command": "sh run | sec router ospf   ",
    #     "recommendations": "Configure the Message Digest option for OSPF. hostname(config)#router ospf <ospf_process-id> hostname(config-router)#area <ospf_area-id> authentication message-digest  Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Configuring the area 'authentication message-digest' for OSPF enforces these policies by restricting exchanges between network devices. Default Value: http://www.cisco.com/en/US/docs/ios-xml/ios/interface/command/ir-i1.html#GUID-0D6BDFCD-3FBB-4D26-A274-C1221F8592DFhttp://www.cisco.com/en/US/docs/ios-xml/ios/interface/command/ir-i1.html#GUID-0D6BDFCD-3FBB-4D26-A274-C1221F8592DFhttp://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-i1.html#GUID-8D1B0697-8E96-4D8A-BD20-536956D68506http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_eigrp/command/ire-i1.html#GUID-8D1B0697-8E96-4D8A-BD20-536956D6850695   Not set  "
    # },
    # {
    #     "title": "3.3.2.2 Set 'ip ospf message-digest-key md5' (Scored) ",
    #     "description": "Enable Open Shortest Path First (OSPF) Message Digest 5 (MD5) authentication.  ",
    #     "audit": "Verify the appropriate md5 key is defined on the appropriate interface(s) hostname#sh run int <interface>  ",
    #     "command": "sh run int <interface>  ",
    #     "recommendations": "Configure the appropriate interface(s) for Message Digest authentication hostname(config)#interface <interface_name> hostname(config-if)#ip ospf message-digest-key {ospf_md5_key-id} md5 {ospf_md5_key} Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Configuring the proper interface(s) for 'ip ospf message-digest-key md5' enforces these policies by restricting exchanges between network devices. Default Value: http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_ospf/command/ospf-i1.html#GUID-3D5781A3-F8DF-4760-A551-6A3AB80A42EDhttp://www.cisco.com/en/US/docs/ios-xml/ios/iproute_ospf/command/ospf-i1.html#GUID-3D5781A3-F8DF-4760-A551-6A3AB80A42EDhttp://www.cisco.com/en/US/docs/ios-xml/ios/iproute_ospf/command/ospf-a1.html#GUID-81D0F753-D8D5-494E-9A10-B15433CFD445http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_ospf/command/ospf-a1.html#GUID-81D0F753-D8D5-494E-9A10-B15433CFD44596   Not set  "
    # },
    # {
    #     "title": "3.3.3.1 Set 'key chain' (Scored) ",
    #     "description": "Define an authentication key chain to enable authentication for RIPv2 routing protocols.  ",
    #     "audit": "Verify the appropriate key chain is defined hostname#sh run | sec key chain   ",
    #     "command": "sh run | sec key chain   ",
    #     "recommendations": "Establish the key chain. hostname(config)#key chain {rip_key-chain_name} http://www.cisco.com/en/US/docs/ios-xml/ios/interface/command/ir-i1.html#GUID-0D6BDFCD-3FBB-4D26-A274-C1221F8592DFhttp://www.cisco.com/en/US/docs/ios-xml/ios/interface/command/ir-i1.html#GUID-0D6BDFCD-3FBB-4D26-A274-C1221F8592DFhttp://www.cisco.com/en/US/docs/ios-xml/ios/iproute_ospf/command/ospf-i1.html#GUID-939C79FF-8C09-4D5A-AEB5-DAF25038CA18http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_ospf/command/ospf-i1.html#GUID-939C79FF-8C09-4D5A-AEB5-DAF25038CA1897   Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Configuring the proper authentication 'key-chain (name)' for RIPv2 protocols enforces these policies by restricting acceptable authentication between network devices. Default Value: Not set  "
    # },
    # {
    #     "title": "3.3.3.2 Set 'key' (Scored) ",
    #     "description": "Configure an authentication key on a key chain.  ",
    #     "audit": "Verify the appropriate key chain is defined hostname#sh run | sec key chain   ",
    #     "command": "sh run | sec key chain   ",
    #     "recommendations": "Configure the key number. hostname(config-keychain)#key {key-number} Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Configuring the proper authentication 'key' http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_pi/command/iri-cr-a1.html#GUID-A62E89F5-0B8B-4CF0-B4EB-08F2762D88BBhttp://www.cisco.com/en/US/docs/ios-xml/ios/iproute_pi/command/iri-cr-a1.html#GUID-A62E89F5-0B8B-4CF0-B4EB-08F2762D88BB98   for RIPv2 protocols enforces these policies by restricting acceptable authentication between network devices.  "
    # },
    # {
    #     "title": "3.3.3.3 Set 'key-string' (Scored) ",
    #     "description": "Configure the authentication string for a key.  ",
    #     "audit": "Verify the appropriate key chain is defined hostname#sh run | sec key chain   ",
    #     "command": "sh run | sec key chain   ",
    #     "recommendations": "Configure the key string. hostname(config-keychain-key)#key-string <key-string>  Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Using 'key-string' for key chains for routing protocols enforces these policies. Default Value: Not set  "
    # },
    # {
    #     "title": "3.3.3.4 Set 'ip rip authentication key-chain' (Scored) ",
    #     "description": "Enable authentication for Routing Information Protocol (RIP) Version 2 packets and to specify the set of keys that can be used on an interface.  ",
    #     "audit": "Verify the appropriate key chain and mode are set on the appropriate interface(s) hostname#sh run int <interface_name>  ",
    #     "command": "sh run int <interface_name>  ",
    #     "recommendations": "Configure the Interface with the RIPv2 key chain. hostname(config)#interface <interface_name> hostname(config-if)#ip rip authentication key-chain {rip_key-chain_name} Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Configuring the interface with 'ip rip authentication key-chain' by name enforces these policies by restricting the exchanges between network devices. Default Value: Not set  "
    # },
    # {
    #     "title": "3.3.3.5 Set 'ip rip authentication mode' to 'md5' (Scored) ",
    #     "description": "Configure the Interface with the RIPv2 key chain.  ",
    #     "audit": "Verify the appropriate mode is set on the appropriate interface(s) hostname#sh run int <interface>   ",
    #     "command": "sh run int <interface>   ",
    #     "recommendations": "Configure the RIPv2 authentication mode on the necessary interface(s) hostname(config)#interface <interface_name> hostname(config-if)#ip rip authentication mode md5  Impact: Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Using the 'ip rip authentication mode md5' enforces these policies by restricting the type of authentication between network devices. Default Value: Not set  "
    # },
    # {
    #     "title": "3.3.4.1 Set 'neighbor password' (Scored) ",
    #     "description": "Enable message digest5 (MD5) authentication on a TCP connection between two BGP peers  ",
    #     "audit": "Verify you see the appropriate neighbor password is defined: hostname#sh run | sec router bgp   ",
    #     "command": "sh run | sec router bgp   ",
    #     "recommendations": "Configure BGP neighbor authentication where feasible. hostname(config)#router bgp <bgp_as-number> hostname(config-router)#neighbor <bgp_neighbor-ip | peer-group-name> password <password>  Impact: http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_rip/command/irr-cr-rip.html#GUID-47536344-60DC-4D30-9E03-94FF336332C7http://www.cisco.com/en/US/docs/ios-xml/ios/iproute_rip/command/irr-cr-rip.html#GUID-47536344-60DC-4D30-9E03-94FF336332C7102   Organizations should plan and implement enterprise security policies that require rigorous authentication methods for routing protocols. Using the 'neighbor password' for BGP enforces these policies by restricting the type of authentication between network devices. Default Value: Not set  "
    # }
]