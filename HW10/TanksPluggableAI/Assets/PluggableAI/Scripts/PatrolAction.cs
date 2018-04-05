using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu (menuName = "PluggableAI/Actions/Patrol")]
public class PatrolAction : Action {

    public override void Act(StateController controller)
    {
        Patrol(controller);
    }

    private void Patrol(StateController controller)
    {
        // Look up next waypoint and walk to it
        controller.navMeshAgent.destination = controller.wayPointList[controller.nextWaypoint].position;
        //controller.navMeshAgent.Resume();
        controller.navMeshAgent.isStopped = false;

        if (controller.navMeshAgent.remainingDistance <= controller.navMeshAgent.stoppingDistance && !controller.navMeshAgent.pathPending)
        {
            // We have arrived at the waypoint, go to the next one
            controller.nextWaypoint = (controller.nextWaypoint + 1) % controller.wayPointList.Count;
        }
    }

}
