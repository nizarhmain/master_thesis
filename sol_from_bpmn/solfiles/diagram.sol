pragma solidity ^0.4.14;


contract Process_0_Contract {
    uint256 tokens = 2;
    address owner = 0;
    address parent = 0;
    uint256 subprocesses = 0;
    uint256[] requestedID;
    event Element_Execution_Completed(uint256 elementId);
    Process_0_WorkList workList = new Process_0_WorkList();
    uint256 active_a = 0;

    function Process_0_Contract() {
        owner = msg.sender;
        for (uint256 i = 0; i < 0; i++) requestedID.push(0);
        step(tokens);
    }

    function setParent(address newParent) {
        if (owner == msg.sender) parent = newParent;
    }

    function handleGlobalDefaultEnd() {
        // ................ Nothing to do ...........
    }

    function handleGlobalErrorEnd(bytes32 eventName) {
        if (parent != 0)
            Process_0_Contract(parent).handleGlobalErrorEnd(eventName);
        else tokens &= uint256(~kill_Process_0());
    }

    function handleGlobalEscalationEnd(bytes32 eventName) {
        if (parent != 0)
            Process_0_Contract(parent).handleGlobalEscalationEnd(eventName);
    }

    function kill_Process_0() returns (uint256) {
        uint256 tokensToKill = 0;
        tokensToKill |= uint256(6);
        active_a = 0;
        tokens &= uint256(~tokensToKill);
        return 0;
    }

    function broadcastSignal_Process_0() {
        // Nothing to do ...
    }

    function a_start(uint256 localTokens) internal returns (uint256) {
        uint256 reqId = workList.DefaultTask_start(this.a_callback);
        active_a |= uint256(1) << reqId;
        return localTokens & uint256(~2);
    }

    function a_callback(uint256 reqId) returns (bool) {
        if (active_a == 0) return false;
        uint256 index = uint256(1) << reqId;
        if (active_a & index == index) {
            active_a &= ~index;

            step(tokens | 4);
            Element_Execution_Completed(1);
            return true;
        }
        return false;
    }

    function EndEvent_1rfz6w8(uint256 localTokens) internal returns (uint256) {
        tokens = localTokens & uint256(~4);
        if (tokens & 6 != 0) {
            return tokens;
        }
        if (parent != 0) Process_0_Contract(parent).handleGlobalDefaultEnd();
        Element_Execution_Completed(2);
        return tokens;
    }

    function step(uint256 localTokens) internal {
        bool done = false;
        while (!done) {
            if (localTokens & 2 == 2) {
                localTokens = a_start(localTokens);
                continue;
            }
            if (localTokens & 4 == 4) {
                localTokens = EndEvent_1rfz6w8(localTokens);
                continue;
            }
            done = true;
        }
        tokens = localTokens;
    }

    function getRunningFlowNodes() returns (uint256) {
        uint256 flowNodes = 0;
        uint256 localTokens = tokens;
        return flowNodes;
    }

    function getStartedFlowNodes() returns (uint256) {
        uint256 flowNodes = 0;
        uint256 localTokens = tokens;
        if (active_a != 0) flowNodes |= 1;

        return flowNodes;
    }

    function getWorkListAddress() returns (address) {
        return workList;
    }

    function getTaskRequestIndex(uint256 taskId) returns (uint256) {
        if (taskId == 1) return active_a;
    }
}


contract Process_0_WorkList {
    struct DefaultTask_Request {
        function(uint256) returns (bool) external callback;
    }
    DefaultTask_Request[] DefaultTask_requests;

    function DefaultTask_start(
        function(uint256) returns (bool) external callback
    ) returns (uint256) {
        uint256 index = DefaultTask_requests.length;
        DefaultTask_requests.push(DefaultTask_Request(callback));
        return index;
    }

    function DefaultTask_callback(uint256 reqId) {
        DefaultTask_requests[reqId].callback(reqId);
    }
}
