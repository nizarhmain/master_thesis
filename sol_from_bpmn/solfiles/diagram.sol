pragma solidity ^0.4.14;
        
    
        
    contract Process_0_Contract {
        uint tokens = 2;
        address owner = 0;
        address parent = 0;
        uint subprocesses = 0;
        uint [] requestedID;
                    event Element_Execution_Completed(uint elementId);
            Process_0_WorkList workList = new Process_0_WorkList();
            uint active_firstask = 0;
                        
        function Process_0_Contract() {
            owner = msg.sender;
                for (uint i = 0; i < 0; i++)
                requestedID.push(0);
            step(tokens);
        }
    
        function setParent(address newParent) {
            if (owner == msg.sender)
                parent = newParent;
        }
    
            function handleGlobalDefaultEnd() {
                // ................ Nothing to do ...........
            }
    
            function handleGlobalErrorEnd(bytes32 eventName) {
                if (parent != 0)
                Process_0_Contract(parent).handleGlobalErrorEnd(eventName);
                else
                tokens &= uint(~kill_Process_0());
             }
    
            function handleGlobalEscalationEnd(bytes32 eventName) {
                if (parent != 0)
                Process_0_Contract(parent).handleGlobalEscalationEnd(eventName);
             }
    
                                function kill_Process_0() returns (uint) {
            uint tokensToKill = 0;
                tokensToKill |= uint(6);
                active_firstask = 0;
                    tokens &= uint(~tokensToKill);
            return 0;   
            }
    
             function broadcastSignal_Process_0() {
            // Nothing to do ...
        }
    
                        
        function firstask_start (uint localTokens) internal returns (uint) {
            uint reqId = workList.DefaultTask_start (this.firstask_callback);
            active_firstask |= uint(1) << reqId;
                return localTokens & uint(~2);
            }
    
        function firstask_callback (uint reqId) returns (bool) {
            if (active_firstask == 0) 
                return false;
            uint index = uint(1) << reqId;
            if(active_firstask & index == index) {
                active_firstask &= ~index;
                    
                step (tokens | 4);
                    Element_Execution_Completed(1);
                return true;
            }
            return false ;
        }
    
            function Event_1y9xp5v(uint localTokens) internal returns (uint) {
            tokens = localTokens & uint(~4);
                if (tokens & 6 != 0) {
                    return tokens;
            }
                if (parent != 0)
                Process_0_Contract(parent).handleGlobalDefaultEnd();
                Element_Execution_Completed(2);
                return tokens;
        }
    
                function step(uint localTokens) internal { 
            bool done = false;
            while (!done) {
                    if (localTokens & 2 == 2) {
                    localTokens = firstask_start(localTokens);
                    continue;
                }
                    if (localTokens & 4 == 4) {
                    localTokens = Event_1y9xp5v(localTokens); 
                    continue;
                }
                        done = true;
            }
            tokens = localTokens;
        }
     
        function getRunningFlowNodes() returns (uint) {
            uint flowNodes = 0;
            uint localTokens = tokens;
                return flowNodes;
        }
    
            function getStartedFlowNodes() returns (uint) {
            uint flowNodes = 0;
            uint localTokens = tokens;
                if(active_firstask != 0)
                flowNodes |= 1;
                
                    return flowNodes;
        }
    
        function getWorkListAddress() returns (address) {
            return workList;
        }
    
        function getTaskRequestIndex(uint taskId) returns (uint) { 
                if (taskId == 1)
                return active_firstask;
            }
    
            }
    
    

contract Process_0_WorkList {
            struct DefaultTask_Request {
            function (uint) external returns (bool) callback;    
        }
        DefaultTask_Request [] DefaultTask_requests;
    
        function DefaultTask_start (function (uint) external returns (bool) callback) returns (uint) {
            uint index = DefaultTask_requests.length;
            DefaultTask_requests.push(DefaultTask_Request(callback));
            return index;
        }
        
        function DefaultTask_callback (uint reqId) {
            DefaultTask_requests[reqId].callback(reqId);
        }
    
        }
    